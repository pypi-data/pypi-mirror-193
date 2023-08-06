import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


class lazy_stats_vx:
    def __init__(self):
        self.data_info = pd.DataFrame()
        self.hypothesis_info = pd.DataFrame()
        self.outlier_info = pd.DataFrame()
        self.dist_list = []

    def data_summary(self, data, indicator=False):
        self.data_info = pd.DataFrame()
        self.data_info['column'] = data.columns.values
        self.data_info['columns_type'] = data.dtypes.values
        self.data_info['null_count'] = data.isna().sum().values
        self.data_info['null_percent'] = np.round_(
            ((data.isna().sum().values / len(data)) * 100), decimals=2)
        self.data_info['unique_values'] = data.nunique().values

        # Percentage of Each Category values , take the mean of their difference for "Balanced Check"
        self.dist_list.clear()
        chk_col = self.data_info[(self.data_info.unique_values <= 10) & (
            self.data_info.unique_values > 1)].column.values
        for col in self.data_info.column.values:
            if col in chk_col:
                uniq_cnt = data[col].value_counts()
                percent = np.sort(
                    ((uniq_cnt.values / (len(data)-data[col].isna().sum())) * 100))
                res = np.mean([percent[i+1] - percent[i]
                              for i in range(len(percent)-1)])
                self.dist_list.append(res)
            else:
                self.dist_list.append(-1)

        self.data_info['dist_balance_chk'] = np.round_(
            self.dist_list, decimals=3)

        self.dist_list.clear()
        for null_p, blnc_chk in zip(self.data_info['null_percent'].values, self.data_info['dist_balance_chk'].values):
            if (blnc_chk >= 50) | (null_p >= 25):
                self.dist_list.append('imbalanced')
            elif (blnc_chk < 50):
                self.dist_list.append('balanced')

        self.data_info['balance_sta'] = self.dist_list
        # data_info['balanc_dic'] = data_info['dist_balanc_chk'].apply( lambda x: 'imbalanced' if x>=50 else 'balanced')

        self.dist_list.clear()
        for val, typ in zip(self.data_info['unique_values'].values, self.data_info['columns_type'].values):
            if val == 2:
                self.dist_list.append('Bin')
            elif (val > 2) & (val < (len(data)/20)):
                self.dist_list.append('Cat')
            else:
                if typ == 'object':
                    self.dist_list.append('Cont_Str')
                else:
                    self.dist_list.append('Cont')

        self.data_info['feature_type'] = self.dist_list

        if indicator == True:
            self.data_info = self.data_info.style.background_gradient(
                cmap="Spectral")

        return self.data_info

    def describe_stats(self, data, columns):
        Result_ST = data[columns].describe()
        Result_ST = Result_ST.transpose()
        variance = []
        mode = []
        median = []
        skew = []
        skew_status = []
        kurtosis = []
        kurtosis_status = []
        for col in Result_ST.index:
            variance.append(data[col].var())
            mode.append(data[col].mode().values[0])
            median.append(data[col].median())
            skew_val = data[col].skew()
            skew.append(skew_val)
            if skew_val == 0:
                skew_status.append('no skew')
            elif skew_val > 0:
                skew_status.append('right skew')
            elif skew_val < 3:
                skew_status.append('left skew')

            kur_val = data[col].kurtosis()
            kurtosis.append(kur_val)
            if kur_val == 3:
                kurtosis_status.append('Mesokurtic')
            elif kur_val > 3:
                kurtosis_status.append('Leptokurtic')
            elif kur_val < 3:
                kurtosis_status.append('Platykurtic')
        Result_ST['variance'] = variance
        Result_ST['mode'] = mode
        Result_ST['median'] = median
        Result_ST['skew'] = skew
        Result_ST['skew_sts'] = skew_status
        Result_ST['kurtosis'] = kurtosis
        Result_ST['kurtosis_sts'] = kurtosis_status
        return Result_ST

    def hypothesis_test(self, data, base_col, columns):
        self.hypothesis_info = pd.DataFrame()
        self.hypothesis_info['column'] = columns
        stat_val = []
        df_val = []
        p_val = []
        p_sts = []
        for col in columns:
            contigency = pd.crosstab(data[base_col], data[col])
            c, p, dof, expected = chi2_contingency(contigency)
            stat_val.append(c)
            df_val.append(dof)
            p_val.append(p)

            significance_level = 0.05
            if p <= significance_level:
                p_sts.append('REJECT NULL HYPOTHESIS')
            else:
                p_sts.append('ACCEPT NULL HYPOTHESIS')

        self.hypothesis_info['Statistical Value'] = stat_val
        self.hypothesis_info['DF Value'] = df_val
        self.hypothesis_info['P Value'] = p_val
        self.hypothesis_info['Status'] = p_sts

        return self.hypothesis_info

    def outlier_check(self, column_value):
        self.outlier_info = pd.DataFrame()
        self.outlier_info['xi'] = np.sort(column_value)
        self.outlier_info['xi - xt'] = np.sort(column_value) - \
            np.median(column_value)
        self.outlier_info['0.67 (xi - xt)'] = 0.6745 * \
            self.outlier_info['xi - xt']
        self.outlier_info['abs(xi - xt)'] = abs(self.outlier_info['xi - xt'])
        self.outlier_info['Mi'] = self.outlier_info['0.67 (xi - xt)'] / np.median(
            self.outlier_info['abs(xi - xt)'])
        out_sts = []
        for val in self.outlier_info['Mi'].values:
            if (-3.5 < val) & (val > 3.5):
                out_sts.append('Outlier')
            else:
                out_sts.append('Inlier')
        self.outlier_info['Status'] = out_sts
        try:
            outlier_percentage = (len(
                self.outlier_info[self.outlier_info['Status'] == 'Outlier']) / len(self.outlier_info)) * 100
        except:
            outlier_percentage = 0
        return self.outlier_info, outlier_percentage

    def cat_column_uper_to_lower(self, data, data_info, col_types='list'):
        categorical_column = data_info[(data_info['feature_type'] == 'Cat') & (
            data_info['columns_type'] == 'object')]
        for col in categorical_column['column'].values:
            data[col] = data[col].str.lower()
        if col_types != 'list':
            categorical_column = data_info[(data_info['feature_type'].isin(
                col_types)) & (data_info['columns_type'] == 'object')]
            for col in categorical_column['column'].values:
                data[col] = data[col].str.lower()
        return data
