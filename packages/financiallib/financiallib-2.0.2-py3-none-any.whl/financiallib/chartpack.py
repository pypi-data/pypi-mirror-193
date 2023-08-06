import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import dataframe_image as dfi

from .plots import return_plots, max_drawdown_plots, rolling_volatility_plots, rolling_max_drawdown_plots
from .plots import plotly_create_subplots, plotly_figure_show, general_plots, plot_returns_heatmap, annualised_periodic_returns, weight_graphs
from .finstats import financial_summary, detailed_summary
from .utils import detailed_summary


# heatmap color
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.templates.default = 'simple_white'

import io
import os

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

import numpy as np

import warnings
warnings.filterwarnings('ignore')


# data preprocessing and plot

class FinancialPlot():
    def __init__(self, detail_summary, price_data_path, strategy, optimization_path, asset_class, pr, period=12, frequency="M", Weights=False, display=True):
        # File names - path

        self.detail_summary = detail_summary
        self.strategy = strategy
        self.optimization_path = optimization_path
        self.asset_class = asset_class
        self.pr = pr
        self.period = period
        self.frequency = frequency
        self.weights_flag = Weights
        self.display = display
        self.price_data_path = price_data_path



    def yearly_returns_data(self, detail_summary):
        self.yearly = detailed_summary(self.detail_summary, sheets=["Portfolio", "Baseline"], period=self.period, prev_yr=self.pr)
        self.yearly = self.yearly[:8]

        return self.yearly


    def detail_summary_data(self, detail_summary):
        self.portfolio = pd.read_excel(self.detail_summary, sheet_name= 'Portfolio', index_col = 0, engine='openpyxl')

        self.baseline = pd.read_excel(self.detail_summary, sheet_name = 'Baseline', engine='openpyxl')

        return self.portfolio, self.baseline

    # data preprocessing
    def statistic_data(self, portfolio, baseline):
        portfolio_stat = portfolio.copy()
        baseline_stat = baseline.copy()

        portfolio_stat.reset_index(inplace=True)

        baseline_stat['returns'] = baseline_stat['Adj Close'].pct_change().dropna()

        return portfolio_stat, baseline_stat

    def cum_ret_data(self, portfolio, baseline):

        baseline.set_index('date', inplace=True)
        cumm_return = pd.concat([portfolio[['invested']], baseline], axis = 1)

        cumm_return.rename(columns = {'invested': 'Portfolio', 'Adj Close' : 'Baseline'}, inplace = True)

        cumm_return.index = pd.to_datetime(cumm_return.index)

        # extra add for riskfolio
        cumm_return = cumm_return[['Portfolio', 'Baseline']]

        return cumm_return

    def calc_beta(self,df):
        np_array = df.values
        s = np_array[:, 0] # stock returns are column zero from numpy array
        m = np_array[:, 1] # market returns are column one from numpy array

        covariance = np.cov(s,m) # Calculate covariance between stock and market
        beta = covariance[0,1]/covariance[1,1]

        return beta

    def rolling_apply(self, df, period, func, min_periods=None):
        if min_periods is None:
            min_periods = period
        result = pd.Series(np.nan, index=df.index)

        for i in range(1, len(df)+1):
            sub_df = df.iloc[max(i-period, 0):i,:] #I edited here
            if len(sub_df) >= min_periods:
                idx = sub_df.index[-1]
                result[idx] = func(sub_df)
        return result

    def rolling_beta_data(self, portfolio, baseline, period_6m = 6, period_12m = 12):

        _portfolio = portfolio.iloc[1:-1]

        _baseline = baseline.iloc[:-1]

        _baseline.index = pd.to_datetime(_baseline.index)
        _baseline = _baseline.resample(self.frequency).last()
        _baseline['mkt_ret_1m'] = _baseline['Adj Close'].pct_change()
        _baseline.reset_index(inplace= True)


        rolling_beta = _portfolio.copy()
        rolling_beta.index = pd.to_datetime(rolling_beta.index)
        rolling_beta.reset_index(inplace=True)
        rolling_beta = pd.merge(rolling_beta, _baseline[['date','mkt_ret_1m']], on = 'date')
        rolling_beta = rolling_beta[['date', 'returns', 'mkt_ret_1m']]

        rolling_beta['6m rolling beta'] = self.rolling_apply(rolling_beta[['returns','mkt_ret_1m']], period_6m, self.calc_beta, min_periods = period_6m)
        rolling_beta['12m rolling beta'] = self.rolling_apply(rolling_beta[['returns','mkt_ret_1m']], period_12m, self.calc_beta, min_periods = period_12m)

        rolling_beta = rolling_beta[['date','6m rolling beta','12m rolling beta']]

        rolling_beta.set_index('date',inplace=True)

        return rolling_beta

    def max_drawdown_data(self, portfolio):
        max_drawdown = portfolio[['invested']]

        max_drawdown.rename(columns = {'invested': 'Portfolio'}, inplace = True)

        return max_drawdown

    def rolling_sharpe_data(self, portfolio):
        _portfolio = portfolio.iloc[1:-1]

        if self.frequency == "M":
            wind_6 = 6
            wind_12 = 12
        elif self.frequency == "W":
            wind_6 = 26
            wind_12 = 52
        elif self.frequency == "D":
            wind_6 = 126
            wind_12 = 252

        # test
        _portfolio['6 months rolling'] = _portfolio.returns.rolling(wind_6).apply(lambda x: (((1+x).prod()-1) / wind_6 * wind_12) / (x.std()*np.sqrt(wind_12)), raw = True)
        _portfolio['12 months rolling'] = _portfolio.returns.rolling(wind_12).apply(lambda x: (((1+x).prod()-1) / wind_12 * wind_12) / (x.std()*np.sqrt(wind_12)), raw = True)
        sharpe_ratio = pd.concat([_portfolio['6 months rolling'],_portfolio['12 months rolling']], axis = 1)

        return sharpe_ratio

    def heatmap_monthly_return_data(self, portfolio):

        # test
        monthly_ret_table = portfolio.copy()
        monthly_ret_table.reset_index(inplace=True)

        monthly_ret_table['date'] = pd.to_datetime(monthly_ret_table['date'])
        monthly_ret_table['year'] = monthly_ret_table['date'].dt.year
        monthly_ret_table['month'] = monthly_ret_table['date'].dt.month
        monthly_ret_table = monthly_ret_table[['year', 'month', 'returns']]
        monthly_ret_table['returns'] = monthly_ret_table['returns']*100
        monthly_ret_table['returns'] = monthly_ret_table['returns'].round(2)
        zmax = max(monthly_ret_table['returns'].max(), abs(monthly_ret_table['returns'].min()))


        monthly_ret_table = monthly_ret_table.set_index(['year', 'month']).unstack(level = -1)
        monthly_ret_table.columns = monthly_ret_table.columns.droplevel()
        monthly_ret_table.columns.name = None
        monthly_ret_table.rename({monthly_ret_table.columns[0]:'Jan', monthly_ret_table.columns[1]:'Feb',
                            monthly_ret_table.columns[2]: 'Mar', monthly_ret_table.columns[3]:'Apr',
                            monthly_ret_table.columns[4]:'May', monthly_ret_table.columns[5]:'Jun',
                            monthly_ret_table.columns[6]: 'Jul', monthly_ret_table.columns[7]:'Aug',
                            monthly_ret_table.columns[8]:'Sep', monthly_ret_table.columns[9]:'Oct',
                            monthly_ret_table.columns[10]:'Nov', monthly_ret_table.columns[11]:'Dec'},
                            axis = 1, inplace=True)
        monthly_ret_table = monthly_ret_table.transpose()

        return monthly_ret_table, zmax

    def annualized_data(self, yearly):

        yearly['Security Name'] = ['Portfolio', 'Portfolio', 'Portfolio', 'Portfolio', 'Baseline', 'Baseline', 'Baseline', 'Baseline']

        annualized = pd.concat([yearly.drop('Security Name', axis=1), yearly['Security Name']], axis=1)
        annualized = annualized.round(2)

        # calculation multiply 100 without sharpe ratio
        annualized = annualized.reset_index().set_index(['index', 'Security Name'])
        annualized.index.names = [None, 'Security Name']
        Y = pd.DataFrame(index=annualized.index, columns=annualized.columns)
        for i in annualized.index:
            for j in annualized.columns:
                if 'Sharpe Ratio' not in i:
                    Y.loc[i, j] = annualized.loc[i, j] * 100
                else:
                    Y.loc[i, j] = annualized.loc[i, j]
        Y = Y.reset_index().set_index('level_0')
        Y.index.name = None


        annualized = Y

        return annualized

    # Statistic and plot
    def statistic_plot(self, portfolio_stat, baseline_stat, strategy):

        data = financial_summary(portfolio_stat, baseline_stat, frequency=self.frequency, asset_class= self.asset_class, title = f'{self.strategy}')

        return data

    def cum_ret_plot(self, cumm_return):
        fig = return_plots(cumm_return, graph_width=800, graph_height=500)

        fig.update_xaxes()
        fig.update_layout(height=400, width=800, title_text=f"Cumulative Return {self.strategy}")

        return fig

    def max_drawdown_plot(self, max_drawdown,strategy):
        fig = max_drawdown_plots(max_drawdown, frequency= self.frequency, graph_width=800, graph_height=500, strategy = strategy)

        fig.update_layout(height=500, width=800, title_text=f"Maximum Drawdown {self.strategy}")

        return fig

    def rolling_beta_plot(self, rolling_beta):
        six_month_mean = rolling_beta['6m rolling beta'].mean()
        twelve_month_mean = rolling_beta['12m rolling beta'].mean()
        fig = general_plots(rolling_beta, frequency= self.frequency, graph_width=800, graph_height=500, strategy = self.strategy)


        fig.add_trace(go.Scatter(y = [six_month_mean, six_month_mean],
                                x = [min(rolling_beta.index), max(rolling_beta.index)],
                                mode = 'lines',
                                line = dict(width=2, dash='dash'),
                                marker_color='green',
                                name = f'Mean 6 months rolling beta')
                    )
        fig.add_trace(go.Scatter(y = [twelve_month_mean, twelve_month_mean],
                                 x = [min(rolling_beta.index), max(rolling_beta.index)],
                                 mode = 'lines',
                                 line = dict(width=2, dash='dash'),
                                 marker_color='red',
                                 name = f'Mean 12 months rolling beta')
                        )
        fig.update_layout(height=500, width=800, title_text=f"Rolling Portfolio Beta {self.strategy}")
        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(title_text="Beta")

        return fig

    def rolling_sharpe_ratio_plot(self, sharpe_ratio):

        six_month_mean = sharpe_ratio['6 months rolling'].mean()
        twelve_month_mean = sharpe_ratio['12 months rolling'].mean()
        fig = general_plots(sharpe_ratio,frequency= self.frequency, graph_width=800, graph_height=500, strategy = self.strategy)


        fig.add_trace(go.Scatter(y = [six_month_mean, six_month_mean],
                                    x = [min(sharpe_ratio.index), max(sharpe_ratio.index)],
                                    mode = 'lines',
                                    line = dict(width=2, dash='dash'),
                                    marker_color='green',
                                    name = f'Mean 6 months rolling sharpe ratio')
                        )
        fig.add_trace(go.Scatter(y = [twelve_month_mean, twelve_month_mean],
                                    x = [min(sharpe_ratio.index), max(sharpe_ratio.index)],
                                    mode = 'lines',
                                    line = dict(width=2, dash='dash'),
                                     marker_color='red',
                                    name = f'Mean 12 months rolling sharpe ratio')
                        )
        fig.update_layout(height=500, width=800, title_text=f"Rolling Sharpe Ratio {self.strategy}")
        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(title_text="Sharpe Ratio")

        return fig

    def heatmap_monthly_return_plot(self, monthly_ret_table, zmax):

        fig = plot_returns_heatmap(monthly_ret_table,frequency = self.frequency, graph_width=800, graph_height=500, strategy = self.strategy, z = zmax)

        fig.update_xaxes(title_text="Year")
        fig.update_yaxes(title_text="Month")

        fig.update_layout(coloraxis = {'colorscale':'RdYlGn'})
        fig.update_xaxes(side="bottom")
        fig.update_coloraxes(colorbar_title_text = 'Return(%)')
        fig.update_layout(
              title=f'Monthly Return {self.strategy}',
              plot_bgcolor='white'
            )

        return fig


    def annualized_plot(self, ann, strategy):

        fig = annualised_periodic_returns(ann, securities = ['Portfolio', 'Baseline'], frequency= self.frequency, graph_width=1200, graph_height=100, strategy = self.strategy)

        fig.update_layout(height=500, width=900, title_text=f"Yearwise Annual Return {self.strategy}")

        return fig

    def weight_plot(self, tic, strategy):

        wfig = weight_graphs(weights_file = self.detail_summary,
                           ticker=tic,
                           threshold = 0.01,
                           path=self.price_data_path,
                           price_col='Adj Close',
                           frequency=self.frequency)

        wfig.update_layout(width=900,
                           height=500,
                           title=f'Weight and Signal Chart ('+tic+')')

        return wfig


    def main_(self):

        # read
        image_path = []
        portfolio, baseline = self.detail_summary_data(self.detail_summary)
        yearly_ = self.yearly_returns_data(self.detail_summary)
        yearly = self.yearly_returns_data(yearly_) #####

        # data
        portfolio_stat, baseline_stat = self.statistic_data(portfolio, baseline)
        cumm_return = self.cum_ret_data(portfolio, baseline)
        rolling_beta = self.rolling_beta_data(portfolio, baseline)
        sharpe_ratio = self.rolling_sharpe_data(portfolio)
        max_drawdown = self.max_drawdown_data(portfolio)
        monthly_ret_table, zmax = self.heatmap_monthly_return_data(portfolio)
        ann = self.annualized_data(yearly)

        # plot

        data = self.statistic_plot(portfolio_stat, baseline_stat, self.strategy)
        dfi.export(data, f'{self.optimization_path}/test.png')
        image_path.append(f'./{self.optimization_path}/test.png')

        image_path.append(f'./{self.optimization_path}/blank.png')


        from .finstats import financial_summary, detailed_summary
        dfi.export(detailed_summary(self.detail_summary, sheets = ['Portfolio', 'Baseline'], prev_yr=self.pr, period = self.period, title=f'YearWise Summary | {self.strategy}'), f'{self.optimization_path}/test_yearly.png')
        image_path.append(f'./{self.optimization_path}/test_yearly.png')

        cum_ret_fig = self.cum_ret_plot(cumm_return)
        cum_ret_fig.write_image(f'{self.optimization_path}/cum_ret_plot.png')
        image_path.append(f'./{self.optimization_path}/cum_ret_plot.png')


        max_drawdown_fig = self.max_drawdown_plot(max_drawdown, self.strategy)
        max_drawdown_fig.write_image(f'{self.optimization_path}/max_drawdown_plot.png')
        image_path.append(f'./{self.optimization_path}/max_drawdown_plot.png')


        rolling_beta_fig = self.rolling_beta_plot(rolling_beta)
        rolling_beta_fig.write_image(f'{self.optimization_path}/rolling_beta_plot.png')
        image_path.append(f'./{self.optimization_path}/rolling_beta_plot.png')


        rolling_sharpe_fig = self.rolling_sharpe_ratio_plot(sharpe_ratio)
        rolling_sharpe_fig.write_image(f'{self.optimization_path}/rolling_sharpe_plot.png')
        image_path.append(f'./{self.optimization_path}/rolling_sharpe_plot.png')


        heatmap_monthly_return_fig = self.heatmap_monthly_return_plot(monthly_ret_table, zmax)
        heatmap_monthly_return_fig.write_image(f'{self.optimization_path}/heatmap_monthly_plot.png')
        image_path.append(f'./{self.optimization_path}/heatmap_monthly_plot.png')


        ann_fig = self.annualized_plot(ann, self.strategy)
        ann_fig.write_image(f'{self.optimization_path}/ann_plot_fig.png')
        image_path.append(f'./{self.optimization_path}/ann_plot_fig.png')

        yearwise_summary = detailed_summary(self.detail_summary, sheets = ['Portfolio', 'Baseline'], prev_yr=self.pr, title=f'{self.strategy}')


        if self.display:
            # Statistic
            display(data)
            display(detailed_summary(self.detail_summary, sheets = ['Portfolio', 'Baseline'], prev_yr=self.pr, period = self.period, title=f'YearWise Summary | {self.strategy}'))

            # Plots
            cum_ret_fig.show()
            max_drawdown_fig.show()
            rolling_beta_fig.show()
            rolling_sharpe_fig.show()
            heatmap_monthly_return_fig.show()
            ann_fig.show()




        tickers = list(pd.read_excel(self.detail_summary, sheet_name="Weights", index_col=0).columns)

        if self.weights_flag:
            for tic in tickers:
                wfig = self.weight_plot(tic, self.strategy)
                wfig.show()
                wfig.write_image(f'{self.optimization_path}/weight_{tic}_fig.png')
                image_path.append(f'./{self.optimization_path}/weight_{tic}_fig.png')

        return image_path
