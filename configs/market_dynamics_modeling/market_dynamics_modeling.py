market_dynamics_model = dict(
    data_path=
    'data/market_dynamics_modeling/second_level_BTC_LOB/2020-09-01-2020-09-01.feather',
    filter_strength=1,
    slope_interval=[1, -1],
    dynamic_number=5,
    max_length_expectation=3600,
    OE_BTC=False,
    PM='',
    process_datafile_path=
    'D:/TradeMaster1.0.0/data/market_dynamics_modeling/second_level_BTC_LOB/BTCUSDT/2020-09-01-2020-09-01_labeled_slice_and_merge_model_5dynamics_minlength60_quantile_labeling.feather',
    market_dynamic_labeling_visualization_paths=[
        'D:/TradeMaster1.0.0/data/market_dynamics_modeling/second_level_BTC_LOB/BTCUSDT/slice_and_merge_model_5dynamics_minlength60_quantile_labeling_BTCUSDT.png'
    ],
    key_indicator='bid1_price',
    timestamp='timestamp',
    tic='BTCUSDT',
    labeling_method='quantile',
    min_length_limit=60,
    merging_metric='DTW_distance',
    merging_threshold=0.0003,
    merging_dynamic_constraint=1,
    type='Linear_Market_Dynamics_Model')
task_name = 'custom'
dataset_name = 'custom'
