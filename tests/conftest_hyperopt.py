from datetime import timedelta


def hyperopt_test_result():
    """
    Sample hyperopt test result, used for some tests.
    """
    hyperopt_res = [
        {
            "loss": 0.4366182531161519,
            "params_dict": {
                "mfi-value": 15,
                "fastd-value": 20,
                "adx-value": 25,
                "rsi-value": 28,
                "mfi-enabled": False,
                "fastd-enabled": True,
                "adx-enabled": True,
                "rsi-enabled": True,
                "trigger": "macd_cross_signal",
                "sell-mfi-value": 88,
                "sell-fastd-value": 97,
                "sell-adx-value": 51,
                "sell-rsi-value": 67,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": False,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-bb_upper",
                "roi_t1": 1190,
                "roi_t2": 541,
                "roi_t3": 408,
                "roi_p1": 0.026035863879169705,
                "roi_p2": 0.12508730043628782,
                "roi_p3": 0.27766427921605896,
                "stoploss": -0.2562930402099556,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 15,
                    "fastd-value": 20,
                    "adx-value": 25,
                    "rsi-value": 28,
                    "mfi-enabled": False,
                    "fastd-enabled": True,
                    "adx-enabled": True,
                    "rsi-enabled": True,
                    "trigger": "macd_cross_signal",
                },
                "sell": {
                    "sell-mfi-value": 88,
                    "sell-fastd-value": 97,
                    "sell-adx-value": 51,
                    "sell-rsi-value": 67,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": False,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-bb_upper",
                },
                "roi": {
                    0: 0.4287874435315165,
                    408: 0.15112316431545753,
                    949: 0.026035863879169705,
                    2139: 0,
                },
                "stoploss": {"stoploss": -0.2562930402099556},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 2,
                "trade_count_long": 2,
                "trade_count_short": 0,
                "wins": 0,
                "draws": 0,
                "losses": 2,
                "profit_mean": -0.01254995,
                "profit_median": -0.012222,
                "profit_total": -0.00125625,
                "profit_total_abs": -2.50999,
                "max_drawdown_account": 0.23,
                "max_drawdown_abs": -0.00125625,
                "holding_avg": timedelta(minutes=3930.0),
                "stake_currency": "BTC",
                "strategy_name": "SampleStrategy",
            },  # noqa: E501
            "results_explanation": "     2 trades. Avg profit  -1.25%. Total profit -0.00125625 BTC (  -2.51Σ%). Avg duration 3930.0 min.",  # noqa: E501
            "total_profit": -0.00125625,
            "current_epoch": 1,
            "is_initial_point": True,
            "is_random": False,
            "is_best": True,
        },
        {
            "loss": 20.0,
            "params_dict": {
                "mfi-value": 17,
                "fastd-value": 38,
                "adx-value": 48,
                "rsi-value": 22,
                "mfi-enabled": True,
                "fastd-enabled": False,
                "adx-enabled": True,
                "rsi-enabled": True,
                "trigger": "macd_cross_signal",
                "sell-mfi-value": 96,
                "sell-fastd-value": 68,
                "sell-adx-value": 63,
                "sell-rsi-value": 81,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": True,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-sar_reversal",
                "roi_t1": 334,
                "roi_t2": 683,
                "roi_t3": 140,
                "roi_p1": 0.06403981740598495,
                "roi_p2": 0.055519840060645045,
                "roi_p3": 0.3253712811342459,
                "stoploss": -0.338070047333259,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 17,
                    "fastd-value": 38,
                    "adx-value": 48,
                    "rsi-value": 22,
                    "mfi-enabled": True,
                    "fastd-enabled": False,
                    "adx-enabled": True,
                    "rsi-enabled": True,
                    "trigger": "macd_cross_signal",
                },  # noqa: E501
                "sell": {
                    "sell-mfi-value": 96,
                    "sell-fastd-value": 68,
                    "sell-adx-value": 63,
                    "sell-rsi-value": 81,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": True,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-sar_reversal",
                },  # noqa: E501
                "roi": {
                    0: 0.4449309386008759,
                    140: 0.11955965746663,
                    823: 0.06403981740598495,
                    1157: 0,
                },  # noqa: E501
                "stoploss": {"stoploss": -0.338070047333259},
            },
            "results_metrics": {
                "total_trades": 1,
                "trade_count_long": 1,
                "trade_count_short": 0,
                "wins": 0,
                "draws": 0,
                "losses": 1,
                "profit_mean": 0.012357,
                "profit_median": -0.012222,
                "profit_total": 6.185e-05,
                "profit_total_abs": 0.12357,
                "max_drawdown_account": 0.23,
                "max_drawdown_abs": -0.00125625,
                "holding_avg": timedelta(minutes=1200.0),
            },  # noqa: E501
            "results_explanation": "     1 trades. Avg profit   0.12%. Total profit  0.00006185 BTC (   0.12Σ%). Avg duration 1200.0 min.",  # noqa: E501
            "total_profit": 6.185e-05,
            "current_epoch": 2,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
        {
            "loss": 14.241196856510731,
            "params_dict": {
                "mfi-value": 25,
                "fastd-value": 16,
                "adx-value": 29,
                "rsi-value": 20,
                "mfi-enabled": False,
                "fastd-enabled": False,
                "adx-enabled": False,
                "rsi-enabled": False,
                "trigger": "macd_cross_signal",
                "sell-mfi-value": 98,
                "sell-fastd-value": 72,
                "sell-adx-value": 51,
                "sell-rsi-value": 82,
                "sell-mfi-enabled": True,
                "sell-fastd-enabled": True,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-macd_cross_signal",
                "roi_t1": 889,
                "roi_t2": 533,
                "roi_t3": 263,
                "roi_p1": 0.04759065393663096,
                "roi_p2": 0.1488819964638463,
                "roi_p3": 0.4102801822104605,
                "stoploss": -0.05394588767607611,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 25,
                    "fastd-value": 16,
                    "adx-value": 29,
                    "rsi-value": 20,
                    "mfi-enabled": False,
                    "fastd-enabled": False,
                    "adx-enabled": False,
                    "rsi-enabled": False,
                    "trigger": "macd_cross_signal",
                },
                "sell": {
                    "sell-mfi-value": 98,
                    "sell-fastd-value": 72,
                    "sell-adx-value": 51,
                    "sell-rsi-value": 82,
                    "sell-mfi-enabled": True,
                    "sell-fastd-enabled": True,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-macd_cross_signal",
                },
                "roi": {
                    0: 0.6067528326109377,
                    263: 0.19647265040047726,
                    796: 0.04759065393663096,
                    1685: 0,
                },
                "stoploss": {"stoploss": -0.05394588767607611},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 621,
                "trade_count_long": 621,
                "trade_count_short": 0,
                "wins": 320,
                "draws": 0,
                "losses": 301,
                "profit_mean": -0.043883302093397747,
                "profit_median": -0.012222,
                "profit_total": -0.13639474,
                "profit_total_abs": -272.515306,
                "max_drawdown_account": 0.25,
                "max_drawdown_abs": -272.515306,
                "holding_avg": timedelta(minutes=1691.207729468599),
            },  # noqa: E501
            "results_explanation": "   621 trades. Avg profit  -0.44%. Total profit -0.13639474 BTC (-272.52Σ%). Avg duration 1691.2 min.",  # noqa: E501
            "total_profit": -0.13639474,
            "current_epoch": 3,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
        {
            "loss": 100000,
            "params_dict": {
                "mfi-value": 13,
                "fastd-value": 35,
                "adx-value": 39,
                "rsi-value": 29,
                "mfi-enabled": True,
                "fastd-enabled": False,
                "adx-enabled": False,
                "rsi-enabled": True,
                "trigger": "macd_cross_signal",
                "sell-mfi-value": 87,
                "sell-fastd-value": 54,
                "sell-adx-value": 63,
                "sell-rsi-value": 93,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": True,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-bb_upper",
                "roi_t1": 1402,
                "roi_t2": 676,
                "roi_t3": 215,
                "roi_p1": 0.06264755784937427,
                "roi_p2": 0.14258587851894644,
                "roi_p3": 0.20671291201040828,
                "stoploss": -0.11818343570194478,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 13,
                    "fastd-value": 35,
                    "adx-value": 39,
                    "rsi-value": 29,
                    "mfi-enabled": True,
                    "fastd-enabled": False,
                    "adx-enabled": False,
                    "rsi-enabled": True,
                    "trigger": "macd_cross_signal",
                },
                "sell": {
                    "sell-mfi-value": 87,
                    "sell-fastd-value": 54,
                    "sell-adx-value": 63,
                    "sell-rsi-value": 93,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": True,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-bb_upper",
                },
                "roi": {
                    0: 0.411946348378729,
                    215: 0.2052334363683207,
                    891: 0.06264755784937427,
                    2293: 0,
                },
                "stoploss": {"stoploss": -0.11818343570194478},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 0,
                "trade_count_long": 0,
                "trade_count_short": 0,
                "wins": 0,
                "draws": 0,
                "losses": 0,
                "profit_mean": None,
                "profit_median": None,
                "profit_total": 0,
                "max_drawdown_account": 0.0,
                "max_drawdown_abs": 0.0,
                "holding_avg": timedelta(),
            },  # noqa: E501
            "results_explanation": "     0 trades. Avg profit    nan%. Total profit  0.00000000 BTC (   0.00Σ%). Avg duration   nan min.",  # noqa: E501
            "total_profit": 0,
            "current_epoch": 4,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,  # noqa: E501
        },
        {
            "loss": 0.22195522184191518,
            "params_dict": {
                "mfi-value": 17,
                "fastd-value": 21,
                "adx-value": 38,
                "rsi-value": 33,
                "mfi-enabled": True,
                "fastd-enabled": False,
                "adx-enabled": True,
                "rsi-enabled": False,
                "trigger": "macd_cross_signal",
                "sell-mfi-value": 87,
                "sell-fastd-value": 82,
                "sell-adx-value": 78,
                "sell-rsi-value": 69,
                "sell-mfi-enabled": True,
                "sell-fastd-enabled": False,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": False,
                "sell-trigger": "sell-macd_cross_signal",
                "roi_t1": 1269,
                "roi_t2": 601,
                "roi_t3": 444,
                "roi_p1": 0.07280999507931168,
                "roi_p2": 0.08946698095898986,
                "roi_p3": 0.1454876733325284,
                "stoploss": -0.18181041180901014,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 17,
                    "fastd-value": 21,
                    "adx-value": 38,
                    "rsi-value": 33,
                    "mfi-enabled": True,
                    "fastd-enabled": False,
                    "adx-enabled": True,
                    "rsi-enabled": False,
                    "trigger": "macd_cross_signal",
                },
                "sell": {
                    "sell-mfi-value": 87,
                    "sell-fastd-value": 82,
                    "sell-adx-value": 78,
                    "sell-rsi-value": 69,
                    "sell-mfi-enabled": True,
                    "sell-fastd-enabled": False,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": False,
                    "sell-trigger": "sell-macd_cross_signal",
                },
                "roi": {
                    0: 0.3077646493708299,
                    444: 0.16227697603830155,
                    1045: 0.07280999507931168,
                    2314: 0,
                },
                "stoploss": {"stoploss": -0.18181041180901014},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 14,
                "trade_count_long": 14,
                "trade_count_short": 0,
                "wins": 6,
                "draws": 0,
                "losses": 8,
                "profit_mean": -0.003539515,
                "profit_median": -0.012222,
                "profit_total": -0.002480140000000001,
                "profit_total_abs": -4.955321,
                "max_drawdown_account": 0.34,
                "max_drawdown_abs": -4.955321,
                "holding_avg": timedelta(minutes=3402.8571428571427),
            },  # noqa: E501
            "results_explanation": "    14 trades. Avg profit  -0.35%. Total profit -0.00248014 BTC (  -4.96Σ%). Avg duration 3402.9 min.",  # noqa: E501
            "total_profit": -0.002480140000000001,
            "current_epoch": 5,
            "is_initial_point": True,
            "is_random": False,
            "is_best": True,
        },
        {
            "loss": 0.545315889154162,
            "params_dict": {
                "mfi-value": 22,
                "fastd-value": 43,
                "adx-value": 46,
                "rsi-value": 20,
                "mfi-enabled": False,
                "fastd-enabled": False,
                "adx-enabled": True,
                "rsi-enabled": True,
                "trigger": "bb_lower",
                "sell-mfi-value": 87,
                "sell-fastd-value": 65,
                "sell-adx-value": 94,
                "sell-rsi-value": 63,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": True,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-macd_cross_signal",
                "roi_t1": 319,
                "roi_t2": 556,
                "roi_t3": 216,
                "roi_p1": 0.06251955472249589,
                "roi_p2": 0.11659519602202795,
                "roi_p3": 0.0953744132197762,
                "stoploss": -0.024551752215582423,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 22,
                    "fastd-value": 43,
                    "adx-value": 46,
                    "rsi-value": 20,
                    "mfi-enabled": False,
                    "fastd-enabled": False,
                    "adx-enabled": True,
                    "rsi-enabled": True,
                    "trigger": "bb_lower",
                },
                "sell": {
                    "sell-mfi-value": 87,
                    "sell-fastd-value": 65,
                    "sell-adx-value": 94,
                    "sell-rsi-value": 63,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": True,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-macd_cross_signal",
                },
                "roi": {
                    0: 0.2744891639643,
                    216: 0.17911475074452382,
                    772: 0.06251955472249589,
                    1091: 0,
                },
                "stoploss": {"stoploss": -0.024551752215582423},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 39,
                "trade_count_long": 39,
                "trade_count_short": 0,
                "wins": 20,
                "draws": 0,
                "losses": 19,
                "profit_mean": -0.0021400679487179478,
                "profit_median": -0.012222,
                "profit_total": -0.0041773,
                "profit_total_abs": -8.346264999999997,
                "max_drawdown_account": 0.45,
                "max_drawdown_abs": -4.955321,
                "holding_avg": timedelta(minutes=636.9230769230769),
            },  # noqa: E501
            "results_explanation": "    39 trades. Avg profit  -0.21%. Total profit -0.00417730 BTC (  -8.35Σ%). Avg duration 636.9 min.",  # noqa: E501
            "total_profit": -0.0041773,
            "current_epoch": 6,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
        {
            "loss": 4.713497421432944,
            "params_dict": {
                "mfi-value": 13,
                "fastd-value": 41,
                "adx-value": 21,
                "rsi-value": 29,
                "mfi-enabled": False,
                "fastd-enabled": True,
                "adx-enabled": False,
                "rsi-enabled": False,
                "trigger": "bb_lower",
                "sell-mfi-value": 99,
                "sell-fastd-value": 60,
                "sell-adx-value": 81,
                "sell-rsi-value": 69,
                "sell-mfi-enabled": True,
                "sell-fastd-enabled": True,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": False,
                "sell-trigger": "sell-macd_cross_signal",
                "roi_t1": 771,
                "roi_t2": 620,
                "roi_t3": 145,
                "roi_p1": 0.0586919200378493,
                "roi_p2": 0.04984118697312542,
                "roi_p3": 0.37521058680247044,
                "stoploss": -0.14613268022709905,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 13,
                    "fastd-value": 41,
                    "adx-value": 21,
                    "rsi-value": 29,
                    "mfi-enabled": False,
                    "fastd-enabled": True,
                    "adx-enabled": False,
                    "rsi-enabled": False,
                    "trigger": "bb_lower",
                },
                "sell": {
                    "sell-mfi-value": 99,
                    "sell-fastd-value": 60,
                    "sell-adx-value": 81,
                    "sell-rsi-value": 69,
                    "sell-mfi-enabled": True,
                    "sell-fastd-enabled": True,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": False,
                    "sell-trigger": "sell-macd_cross_signal",
                },
                "roi": {
                    0: 0.4837436938134452,
                    145: 0.10853310701097472,
                    765: 0.0586919200378493,
                    1536: 0,
                },  # noqa: E501
                "stoploss": {"stoploss": -0.14613268022709905},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 318,
                "trade_count_long": 318,
                "trade_count_short": 0,
                "wins": 100,
                "draws": 0,
                "losses": 218,
                "profit_mean": -0.0039833954716981146,
                "profit_median": -0.012222,
                "profit_total": -0.06339929,
                "profit_total_abs": -126.67197600000004,
                "max_drawdown_account": 0.50,
                "max_drawdown_abs": -200.955321,
                "holding_avg": timedelta(minutes=3140.377358490566),
            },  # noqa: E501
            "results_explanation": "   318 trades. Avg profit  -0.40%. Total profit -0.06339929 BTC (-126.67Σ%). Avg duration 3140.4 min.",  # noqa: E501
            "total_profit": -0.06339929,
            "current_epoch": 7,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
        {
            "loss": 20.0,  # noqa: E501
            "params_dict": {
                "mfi-value": 24,
                "fastd-value": 43,
                "adx-value": 33,
                "rsi-value": 20,
                "mfi-enabled": False,
                "fastd-enabled": True,
                "adx-enabled": True,
                "rsi-enabled": True,
                "trigger": "sar_reversal",
                "sell-mfi-value": 89,
                "sell-fastd-value": 74,
                "sell-adx-value": 70,
                "sell-rsi-value": 70,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": False,
                "sell-adx-enabled": False,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-sar_reversal",
                "roi_t1": 1149,
                "roi_t2": 375,
                "roi_t3": 289,
                "roi_p1": 0.05571820757172588,
                "roi_p2": 0.0606240398618907,
                "roi_p3": 0.1729012220156157,
                "stoploss": -0.1588514289110401,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 24,
                    "fastd-value": 43,
                    "adx-value": 33,
                    "rsi-value": 20,
                    "mfi-enabled": False,
                    "fastd-enabled": True,
                    "adx-enabled": True,
                    "rsi-enabled": True,
                    "trigger": "sar_reversal",
                },
                "sell": {
                    "sell-mfi-value": 89,
                    "sell-fastd-value": 74,
                    "sell-adx-value": 70,
                    "sell-rsi-value": 70,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": False,
                    "sell-adx-enabled": False,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-sar_reversal",
                },
                "roi": {
                    0: 0.2892434694492323,
                    289: 0.11634224743361658,
                    664: 0.05571820757172588,
                    1813: 0,
                },
                "stoploss": {"stoploss": -0.1588514289110401},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 1,
                "trade_count_long": 1,
                "trade_count_short": 0,
                "wins": 0,
                "draws": 1,
                "losses": 0,
                "profit_mean": 0.0,
                "profit_median": 0.0,
                "profit_total": 0.0,
                "profit_total_abs": 0.0,
                "max_drawdown_account": 0.0,
                "max_drawdown_abs": 0.52,
                "holding_avg": timedelta(minutes=5340.0),
            },  # noqa: E501
            "results_explanation": "     1 trades. Avg profit   0.00%. Total profit  0.00000000 BTC (   0.00Σ%). Avg duration 5340.0 min.",  # noqa: E501
            "total_profit": 0.0,
            "current_epoch": 8,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
        {
            "loss": 2.4731817780991223,
            "params_dict": {
                "mfi-value": 22,
                "fastd-value": 20,
                "adx-value": 29,
                "rsi-value": 40,
                "mfi-enabled": False,
                "fastd-enabled": False,
                "adx-enabled": False,
                "rsi-enabled": False,
                "trigger": "sar_reversal",
                "sell-mfi-value": 97,
                "sell-fastd-value": 65,
                "sell-adx-value": 81,
                "sell-rsi-value": 64,
                "sell-mfi-enabled": True,
                "sell-fastd-enabled": True,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-bb_upper",
                "roi_t1": 1012,
                "roi_t2": 584,
                "roi_t3": 422,
                "roi_p1": 0.036764323603472565,
                "roi_p2": 0.10335480573205287,
                "roi_p3": 0.10322347377503042,
                "stoploss": -0.2780610808108503,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 22,
                    "fastd-value": 20,
                    "adx-value": 29,
                    "rsi-value": 40,
                    "mfi-enabled": False,
                    "fastd-enabled": False,
                    "adx-enabled": False,
                    "rsi-enabled": False,
                    "trigger": "sar_reversal",
                },
                "sell": {
                    "sell-mfi-value": 97,
                    "sell-fastd-value": 65,
                    "sell-adx-value": 81,
                    "sell-rsi-value": 64,
                    "sell-mfi-enabled": True,
                    "sell-fastd-enabled": True,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-bb_upper",
                },
                "roi": {
                    0: 0.2433426031105559,
                    422: 0.14011912933552545,
                    1006: 0.036764323603472565,
                    2018: 0,
                },
                "stoploss": {"stoploss": -0.2780610808108503},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 229,
                "trade_count_long": 229,
                "trade_count_short": 0,
                "wins": 150,
                "draws": 0,
                "losses": 79,
                "profit_mean": -0.0038433433624454144,
                "profit_median": -0.012222,
                "profit_total": -0.044050070000000004,
                "profit_total_abs": -88.01256299999999,
                "max_drawdown_account": 0.41,
                "max_drawdown_abs": -150.955321,
                "holding_avg": timedelta(minutes=6505.676855895196),
            },  # noqa: E501
            "results_explanation": "   229 trades. Avg profit  -0.38%. Total profit -0.04405007 BTC ( -88.01Σ%). Avg duration 6505.7 min.",  # noqa: E501
            "total_profit": -0.044050070000000004,  # noqa: E501
            "current_epoch": 9,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
        {
            "loss": -0.2604606005845212,  # noqa: E501
            "params_dict": {
                "mfi-value": 23,
                "fastd-value": 24,
                "adx-value": 22,
                "rsi-value": 24,
                "mfi-enabled": False,
                "fastd-enabled": False,
                "adx-enabled": False,
                "rsi-enabled": True,
                "trigger": "macd_cross_signal",
                "sell-mfi-value": 97,
                "sell-fastd-value": 70,
                "sell-adx-value": 64,
                "sell-rsi-value": 80,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": True,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-sar_reversal",
                "roi_t1": 792,
                "roi_t2": 464,
                "roi_t3": 215,
                "roi_p1": 0.04594053535385903,
                "roi_p2": 0.09623192684243963,
                "roi_p3": 0.04428219070850663,
                "stoploss": -0.16992287161634415,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 23,
                    "fastd-value": 24,
                    "adx-value": 22,
                    "rsi-value": 24,
                    "mfi-enabled": False,
                    "fastd-enabled": False,
                    "adx-enabled": False,
                    "rsi-enabled": True,
                    "trigger": "macd_cross_signal",
                },
                "sell": {
                    "sell-mfi-value": 97,
                    "sell-fastd-value": 70,
                    "sell-adx-value": 64,
                    "sell-rsi-value": 80,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": True,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-sar_reversal",
                },
                "roi": {
                    0: 0.18645465290480528,
                    215: 0.14217246219629864,
                    679: 0.04594053535385903,
                    1471: 0,
                },
                "stoploss": {"stoploss": -0.16992287161634415},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 4,
                "trade_count_long": 4,
                "trade_count_short": 0,
                "wins": 0,
                "draws": 0,
                "losses": 4,
                "profit_mean": 0.001080385,
                "profit_median": -0.012222,
                "profit_total": 0.00021629,
                "profit_total_abs": 0.432154,
                "max_drawdown_account": 0.13,
                "max_drawdown_abs": -4.955321,
                "holding_avg": timedelta(minutes=2850.0),
            },  # noqa: E501
            "results_explanation": "     4 trades. Avg profit   0.11%. Total profit  0.00021629 BTC (   0.43Σ%). Avg duration 2850.0 min.",  # noqa: E501
            "total_profit": 0.00021629,
            "current_epoch": 10,
            "is_initial_point": True,
            "is_random": False,
            "is_best": True,
        },
        {
            "loss": 4.876465945994304,  # noqa: E501
            "params_dict": {
                "mfi-value": 20,
                "fastd-value": 32,
                "adx-value": 49,
                "rsi-value": 23,
                "mfi-enabled": True,
                "fastd-enabled": True,
                "adx-enabled": False,
                "rsi-enabled": False,
                "trigger": "bb_lower",
                "sell-mfi-value": 75,
                "sell-fastd-value": 56,
                "sell-adx-value": 61,
                "sell-rsi-value": 62,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": False,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-macd_cross_signal",
                "roi_t1": 579,
                "roi_t2": 614,
                "roi_t3": 273,
                "roi_p1": 0.05307643172744114,
                "roi_p2": 0.1352282078262871,
                "roi_p3": 0.1913307406325751,
                "stoploss": -0.25728526022513887,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 20,
                    "fastd-value": 32,
                    "adx-value": 49,
                    "rsi-value": 23,
                    "mfi-enabled": True,
                    "fastd-enabled": True,
                    "adx-enabled": False,
                    "rsi-enabled": False,
                    "trigger": "bb_lower",
                },
                "sell": {
                    "sell-mfi-value": 75,
                    "sell-fastd-value": 56,
                    "sell-adx-value": 61,
                    "sell-rsi-value": 62,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": False,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-macd_cross_signal",
                },
                "roi": {
                    0: 0.3796353801863034,
                    273: 0.18830463955372825,
                    887: 0.05307643172744114,
                    1466: 0,
                },
                "stoploss": {"stoploss": -0.25728526022513887},
            },  # noqa: E501
            # New Hyperopt mode!
            "results_metrics": {
                "total_trades": 117,
                "trade_count_long": 117,
                "trade_count_short": 0,
                "wins": 67,
                "draws": 0,
                "losses": 50,
                "profit_mean": -0.012698609145299145,
                "profit_median": -0.012222,
                "profit_total": -0.07436117,
                "profit_total_abs": -148.573727,
                "max_drawdown_account": 0.52,
                "max_drawdown_abs": -224.955321,
                "holding_avg": timedelta(minutes=4282.5641025641025),
            },  # noqa: E501
            "results_explanation": "   117 trades. Avg profit  -1.27%. Total profit -0.07436117 BTC (-148.57Σ%). Avg duration 4282.6 min.",  # noqa: E501
            "total_profit": -0.07436117,
            "current_epoch": 11,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
        {
            "loss": 100000,
            "params_dict": {
                "mfi-value": 10,
                "fastd-value": 36,
                "adx-value": 31,
                "rsi-value": 22,
                "mfi-enabled": True,
                "fastd-enabled": True,
                "adx-enabled": True,
                "rsi-enabled": False,
                "trigger": "sar_reversal",
                "sell-mfi-value": 80,
                "sell-fastd-value": 71,
                "sell-adx-value": 60,
                "sell-rsi-value": 85,
                "sell-mfi-enabled": False,
                "sell-fastd-enabled": False,
                "sell-adx-enabled": True,
                "sell-rsi-enabled": True,
                "sell-trigger": "sell-bb_upper",
                "roi_t1": 1156,
                "roi_t2": 581,
                "roi_t3": 408,
                "roi_p1": 0.06860454019988212,
                "roi_p2": 0.12473718444931989,
                "roi_p3": 0.2896360635226823,
                "stoploss": -0.30889015124682806,
            },  # noqa: E501
            "params_details": {
                "buy": {
                    "mfi-value": 10,
                    "fastd-value": 36,
                    "adx-value": 31,
                    "rsi-value": 22,
                    "mfi-enabled": True,
                    "fastd-enabled": True,
                    "adx-enabled": True,
                    "rsi-enabled": False,
                    "trigger": "sar_reversal",
                },
                "sell": {
                    "sell-mfi-value": 80,
                    "sell-fastd-value": 71,
                    "sell-adx-value": 60,
                    "sell-rsi-value": 85,
                    "sell-mfi-enabled": False,
                    "sell-fastd-enabled": False,
                    "sell-adx-enabled": True,
                    "sell-rsi-enabled": True,
                    "sell-trigger": "sell-bb_upper",
                },
                "roi": {
                    0: 0.4829777881718843,
                    408: 0.19334172464920202,
                    989: 0.06860454019988212,
                    2145: 0,
                },
                "stoploss": {"stoploss": -0.30889015124682806},
            },  # noqa: E501
            "results_metrics": {
                "total_trades": 0,
                "trade_count_long": 0,
                "trade_count_short": 0,
                "wins": 0,
                "draws": 0,
                "losses": 0,
                "profit_mean": None,
                "profit_median": None,
                "profit_total": 0,
                "profit_total_abs": 0.0,
                "max_drawdown_account": 0.0,
                "max_drawdown_abs": 0.0,
                "holding_avg": timedelta(),
            },  # noqa: E501
            "results_explanation": "     0 trades. Avg profit    nan%. Total profit  0.00000000 BTC (   0.00Σ%). Avg duration   nan min.",  # noqa: E501
            "total_profit": 0,
            "current_epoch": 12,
            "is_initial_point": True,
            "is_random": False,
            "is_best": False,
        },
    ]

    for res in hyperopt_res:
        res["results_metrics"]["holding_avg_s"] = res["results_metrics"][
            "holding_avg"
        ].total_seconds()
    return hyperopt_res
