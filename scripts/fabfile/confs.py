confs = {
        "local_lineitem" : {
            'JAR' : '/Users/anil/Dev/repos/mdindex/build/libs/mdindex-all.jar',
            'CONF' : '/Users/anil/Dev/repos/mdindex/conf/main.properties',
            'INPUTSDIR' : '/Users/anil/Dev/repos/tpch-dbgen/lineitem1/',
            'HDFSDIR' : '/user/mdindex/lineitem/',
            'TABLENAME': 'lineitem',
            'HOMEDIR' : '/Users/anil/',
            'HADOOPBIN' : '/Users/anil/Dev/tools/hadoop-2.6.0/bin/',
            'SAMPLINGRATE' : '0.1',
            'DELIMITER': '|',
            'NUMTUPLES': '6001215',
            'NUMBUCKETS' : '16',
            'NUMFIELDS' : '16',
            'SCHEMA': 'l_orderkey long, l_partkey int, l_suppkey int, l_linenumber int, l_quantity double, l_extendedprice double, l_discount double, l_tax double, l_returnflag string,  l_linestatus string, l_shipdate date, l_commitdate date, l_receiptdate date, l_shipinstruct string, l_shipmode string, l_comment string',
            'USER': 'anil',
            'HOSTS': ['localhost'],
            'ROLEDEFS': { 'master': ['localhost'] }
            },
        "lineitem": {
            'JAR' : '/data/mdindex/jars/mdindex-all.jar',
            'CONF' : '/home/mdindex/cartilage.properties',
            'INPUTSDIR' : '/data/mdindex/lineitem1000/',
            'HDFSDIR' : '/user/mdindex/lineitem1000/',
            'HOMEDIR' : '/home/mdindex/',
            'TABLENAME' : 'lineitem',
            'HADOOPBIN' : '~/hadoop-2.6.0/bin/',
            'SAMPLINGRATE' : '0.0002',
            'DELIMITER': '|',
            'NUMBUCKETS' : '8192',
            'NUMTUPLES' : '6000000000',
            'NUMFIELDS' : '16',
            'SCHEMA': 'l_orderkey long, l_partkey int, l_suppkey int, l_linenumber int, l_quantity double, l_extendedprice double, l_discount double, l_tax double, l_returnflag string,  l_linestatus string, l_shipdate date, l_commitdate date, l_receiptdate date, l_shipinstruct string, l_shipmode string, l_comment string',
            'USER' : 'mdindex',
            'HOSTS' : ['istc2.csail.mit.edu', 'istc5.csail.mit.edu', 'istc6.csail.mit.edu', 'istc7.csail.mit.edu', 'istc8.csail.mit.edu', 'istc9.csail.mit.edu', 'istc10.csail.mit.edu', 'istc11.csail.mit.edu', 'istc12.csail.mit.edu', 'istc13.csail.mit.edu'],
            'ROLEDEFS' : { 'master': ['istc2.csail.mit.edu'] },
            },
        "local_tpch" : {
            'JAR' : '/Users/anil/Dev/repos/mdindex/build/libs/mdindex-all.jar',
            'CONF' : '/Users/anil/Dev/repos/mdindex/conf/main.properties',
            'INPUTSDIR' : '/Users/anil/Dev/repos/tpch-dbgen/tpchd1',
            'TABLENAME' : 'tpch',
            'HDFSDIR' : '/user/mdindex',
            'HOMEDIR' : '/Users/anil',
            'HADOOPBIN' : '/Users/anil/Dev/tools/hadoop-2.6.0/bin',
            'SAMPLINGRATE' : '0.1',
            'DELIMITER': '|',
            'NUMBUCKETS' : '16',
            'NUMTUPLES': '6001215',
            'NUMFIELDS' : '38',
            'SCHEMA': 'l_linenumber int, l_quantity double, l_extendedprice double, l_discount double, l_tax double, l_returnflag string,  l_linestatus string, l_shipdate date, l_commitdate date, l_receiptdate date, l_shipinstruct string, l_shipmode string, o_orderstatus string, o_totalprice double, o_orderdate date, o_orderpriority string, o_clerk string, o_shippriority int, p_name string, p_mfgr string, p_brand string, p_type string, p_size int, p_container string, p_retailprice double, s_name string, s_address string, s_phone string, s_acctbal double, s_nation string, s_region string, c_name string, c_address string, c_phone string, c_acctbal double, c_mktsegment string, c_nation string, c_region string',
            'USER': 'anil',
            'HOSTS': ['localhost'],
            'ROLEDEFS': { 'master': ['localhost'] }
            },
        "tpch": {
                'JAR' : '/data/mdindex/jars/mdindex-all.jar',
                'CONF' : '/home/mdindex/tpch.properties',
                'TABLENAME' : 'tpch',
                'INPUTSDIR' : '/data/mdindex/tpch/',
                'HDFSDIR' : '/user/mdindex/tpch/',
                'HOMEDIR' : '/home/mdindex/',
                'HADOOPBIN' : '~/hadoop-2.6.0/bin/',
                'SAMPLINGRATE' : '0.002',
                'DELIMITER': '|',
                'NUMBUCKETS' : '4096',
                'NUMTUPLES' : '600000000',
                'NUMFIELDS' : '38',
                'SCHEMA': 'l_linenumber int, l_quantity double, l_extendedprice double, l_discount double, l_tax double, l_returnflag string,  l_linestatus string, l_shipdate date, l_commitdate date, l_receiptdate date, l_shipinstruct string, l_shipmode string, o_orderstatus string, o_totalprice double, o_orderdate date, o_orderpriority string, o_clerk string, o_shippriority int, p_name string, p_mfgr string, p_brand string, p_type string, p_size int, p_container string, p_retailprice double, s_name string, s_address string, s_phone string, s_acctbal double, s_nation string, s_region string, c_name string, c_address string, c_phone string, c_acctbal double, c_mktsegment string, c_nation string, c_region string',
                'USER' : 'mdindex',
                'HOSTS' : ['istc2.csail.mit.edu', 'istc5.csail.mit.edu', 'istc6.csail.mit.edu', 'istc7.csail.mit.edu', 'istc8.csail.mit.edu', 'istc9.csail.mit.edu', 'istc10.csail.mit.edu', 'istc11.csail.mit.edu', 'istc12.csail.mit.edu', 'istc13.csail.mit.edu'],
                'ROLEDEFS' : { 'master': ['istc2.csail.mit.edu'] },
                },
        "local_cmt" : {
                'JAR' : '/Users/anil/Dev/repos/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/anil/Dev/repos/mdindex/conf/cmt.properties',
                'INPUTSDIR' : '/Users/anil/Dev/data/cmt1/',
                'HDFSDIR' : '/user/mdindex/cmt1/',
                'HOMEDIR' : '/Users/anil/',
                'HADOOPBIN' : '/Users/anil/Dev/tools/hadoop-2.6.0/bin/',
                'SAMPLINGRATE' : '0.1',
                'DELIMITER': '$',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '500000',
                'NUMFIELDS' : '148',
                'SCHEMA': 'mh_id INT,mh_dataset_id STRING,mh_uploadtime DATE,mh_runtime STRING,mh_trip_start DATE,mh_data_count_minutes STRING,mh_data_count_accel_samples STRING,mh_data_count_netloc_samples STRING,mh_data_count_gps_samples STRING,mh_observed_sample_rate STRING,mh_distance_mapmatched_km STRING,mh_distance_gps_km STRING,mh_ground_truth_present STRING,mh_timing_mapmatch DOUBLE,mh_distance_pct_path_error STRING,mh_build_version STRING,mh_timing_queue_wait DOUBLE,mh_data_trip_length STRING,mh_battery_maximum_level STRING,mh_battery_minimum_level STRING,mh_battery_drain_rate_per_hour STRING,mh_battery_plugged_duration_hours STRING,mh_battery_delay_from_drive_end_seconds STRING,mh_startlat STRING,mh_startlon STRING,mh_endlat STRING,mh_endlon STRING,mh_data_count_output_gps_speeding_points STRING,mh_speeding_slow_gps_points STRING,mh_speeding_10kmh_gps_points STRING,mh_speeding_20kmh_gps_points STRING,mh_speeding_40kmh_gps_points STRING,mh_speeding_80kmh_gps_points STRING,mh_output_accel_valid_minutes STRING,mh_output_gps_moving_minutes STRING,mh_output_gps_moving_and_accel_valid_minutes STRING,mh_data_time_till_first_gps_minutes STRING,mh_score_di_accel STRING,mh_score_di_brake STRING,mh_score_di_turn STRING,mh_score_di_car_motion STRING,mh_score_di_phone_motion STRING,mh_score_di_speeding STRING,mh_score_di_night STRING,mh_star_rating STRING,mh_trip_end DATE,mh_score_di_car_motion_with_accel STRING,mh_score_di_car_motion_with_speeding STRING,mh_score_di_distance_km_with_accel STRING,mh_score_di_distance_km_with_speeding STRING,mh_score_accel_per_sec_ntile STRING,mh_score_brake_per_sec_ntile STRING,mh_score_turn_per_sec_ntile STRING,mh_score_speeding_per_sec_ntile STRING,mh_score_phone_motion_per_sec_ntile STRING,mh_score_accel_per_km_ntile STRING,mh_score_brake_per_km_ntile STRING,mh_score_turn_per_km_ntile STRING,mh_score_speeding_per_km_ntile STRING,mh_score_phone_motion_per_km_ntile STRING,mh_score STRING,mh_distance_prepended_km STRING,mh_recording_start DATE,mh_score_di_distance_km STRING,mh_recording_end DATE,mh_recording_startlat STRING,mh_recording_startlon STRING,mh_display_distance_km STRING,mh_display_trip_start DATE,mh_display_startlat STRING,mh_display_startlon STRING,mh_data_count_gyro_samples STRING,mh_star_rating_accel STRING,mh_star_rating_brake STRING,mh_star_rating_turn STRING,mh_star_rating_speeding STRING,mh_star_rating_phone_motion STRING,mh_is_night STRING,mh_battery_total_drain STRING,mh_battery_total_drain_duration_hours STRING,mh_score_smoothness STRING,mh_score_awareness STRING,mh_star_rating_night STRING,mh_star_rating_smoothness STRING,mh_star_rating_awareness STRING,mh_hide STRING,mh_data_count_tag_accel_samples STRING,mh_quat_i STRING,mh_quat_j STRING,mh_quat_k STRING,mh_quat_r STRING,mh_passenger_star_rating STRING,mh_suspension_damping_ratio STRING,mh_suspension_natural_frequency STRING,mh_suspension_fit_error STRING,mh_driving STRING,mh_trip_mode STRING,mh_classification_confidence STRING,mh_gk_trip_mode STRING,mh_gk_confidence STRING,mh_offroad_trip_mode STRING,mh_offroad_confidence STRING,mh_driver_confidence STRING,mh_timing_processing_preprocessing DOUBLE,mh_timing_processing_gatekeeper DOUBLE,mh_timing_processing_accelpipeline DOUBLE,mh_timing_processing_offroad DOUBLE,mh_timing_processing_suspension DOUBLE,mh_timing_processing_scoring DOUBLE,mh_timing_processing_hitchhiker DOUBLE,mh_data_count_obd_samples STRING,mh_data_count_pressure_samples STRING,mh_raw_sampling_mode STRING,mh_data_count_magnetometer_samples STRING,mh_location_disabled_date DATE,sf_id INT,sf_uploadtime DATE,sf_deviceid STRING,sf_driveid STRING,sf_state INT,sf_dest_server STRING,sf_companyid INT,sf_hardware_manufacturer STRING,sf_hardware_model STRING,sf_hardware_bootloader STRING,sf_hardware_build STRING,sf_hardware_carrier STRING,sf_android_fw_version STRING,sf_android_api_version STRING,sf_android_codename STRING,sf_android_baseband STRING,sf_raw_hardware_string STRING,sf_raw_os_string STRING,sf_utc_offset_with_dst STRING,sf_app_version STRING,sf_file_format STRING,sf_start_reason STRING,sf_stop_reason STRING,sf_previous_driveid STRING,sf_userid STRING,sf_tag_mac_address STRING,sf_tag_trip_number STRING,sf_primary_driver_app_user_id STRING,sf_tag_last_connection_number STRING,sf_gps_points_lsh_key_1 STRING,sf_gps_points_lsh_key_2 STRING,sf_gps_points_lsh_key_3 STRING,sf_hidden_by_support STRING',
                'USER': 'anil',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "cmt": {
                'JAR' : '/data/mdindex/jars/mdindex-all.jar',
                'CONF' : '/home/mdindex/cmt.properties',
                'INPUTSDIR' : '/data/mdindex/cmt100/',
                'HDFSDIR' : '/user/mdindex/cmtd100/',
                'HOMEDIR' : '/home/mdindex/',
                'HADOOPBIN' : '~/hadoop-2.6.0/bin/',
                'SAMPLINGRATE' : '0.004',
                'DELIMITER': '$',
                'NUMBUCKETS' : '2048',
                'NUMTUPLES' : '100000000',
                'NUMFIELDS' : '148',
                'SCHEMA': 'mh_id INT,mh_dataset_id STRING,mh_uploadtime DATE,mh_runtime STRING,mh_trip_start DATE,mh_data_count_minutes STRING,mh_data_count_accel_samples STRING,mh_data_count_netloc_samples STRING,mh_data_count_gps_samples STRING,mh_observed_sample_rate STRING,mh_distance_mapmatched_km STRING,mh_distance_gps_km STRING,mh_ground_truth_present STRING,mh_timing_mapmatch DOUBLE,mh_distance_pct_path_error STRING,mh_build_version STRING,mh_timing_queue_wait DOUBLE,mh_data_trip_length STRING,mh_battery_maximum_level STRING,mh_battery_minimum_level STRING,mh_battery_drain_rate_per_hour STRING,mh_battery_plugged_duration_hours STRING,mh_battery_delay_from_drive_end_seconds STRING,mh_startlat STRING,mh_startlon STRING,mh_endlat STRING,mh_endlon STRING,mh_data_count_output_gps_speeding_points STRING,mh_speeding_slow_gps_points STRING,mh_speeding_10kmh_gps_points STRING,mh_speeding_20kmh_gps_points STRING,mh_speeding_40kmh_gps_points STRING,mh_speeding_80kmh_gps_points STRING,mh_output_accel_valid_minutes STRING,mh_output_gps_moving_minutes STRING,mh_output_gps_moving_and_accel_valid_minutes STRING,mh_data_time_till_first_gps_minutes STRING,mh_score_di_accel STRING,mh_score_di_brake STRING,mh_score_di_turn STRING,mh_score_di_car_motion STRING,mh_score_di_phone_motion STRING,mh_score_di_speeding STRING,mh_score_di_night STRING,mh_star_rating STRING,mh_trip_end DATE,mh_score_di_car_motion_with_accel STRING,mh_score_di_car_motion_with_speeding STRING,mh_score_di_distance_km_with_accel STRING,mh_score_di_distance_km_with_speeding STRING,mh_score_accel_per_sec_ntile STRING,mh_score_brake_per_sec_ntile STRING,mh_score_turn_per_sec_ntile STRING,mh_score_speeding_per_sec_ntile STRING,mh_score_phone_motion_per_sec_ntile STRING,mh_score_accel_per_km_ntile STRING,mh_score_brake_per_km_ntile STRING,mh_score_turn_per_km_ntile STRING,mh_score_speeding_per_km_ntile STRING,mh_score_phone_motion_per_km_ntile STRING,mh_score STRING,mh_distance_prepended_km STRING,mh_recording_start DATE,mh_score_di_distance_km STRING,mh_recording_end DATE,mh_recording_startlat STRING,mh_recording_startlon STRING,mh_display_distance_km STRING,mh_display_trip_start DATE,mh_display_startlat STRING,mh_display_startlon STRING,mh_data_count_gyro_samples STRING,mh_star_rating_accel STRING,mh_star_rating_brake STRING,mh_star_rating_turn STRING,mh_star_rating_speeding STRING,mh_star_rating_phone_motion STRING,mh_is_night STRING,mh_battery_total_drain STRING,mh_battery_total_drain_duration_hours STRING,mh_score_smoothness STRING,mh_score_awareness STRING,mh_star_rating_night STRING,mh_star_rating_smoothness STRING,mh_star_rating_awareness STRING,mh_hide STRING,mh_data_count_tag_accel_samples STRING,mh_quat_i STRING,mh_quat_j STRING,mh_quat_k STRING,mh_quat_r STRING,mh_passenger_star_rating STRING,mh_suspension_damping_ratio STRING,mh_suspension_natural_frequency STRING,mh_suspension_fit_error STRING,mh_driving STRING,mh_trip_mode STRING,mh_classification_confidence STRING,mh_gk_trip_mode STRING,mh_gk_confidence STRING,mh_offroad_trip_mode STRING,mh_offroad_confidence STRING,mh_driver_confidence STRING,mh_timing_processing_preprocessing DOUBLE,mh_timing_processing_gatekeeper DOUBLE,mh_timing_processing_accelpipeline DOUBLE,mh_timing_processing_offroad DOUBLE,mh_timing_processing_suspension DOUBLE,mh_timing_processing_scoring DOUBLE,mh_timing_processing_hitchhiker DOUBLE,mh_data_count_obd_samples STRING,mh_data_count_pressure_samples STRING,mh_raw_sampling_mode STRING,mh_data_count_magnetometer_samples STRING,mh_location_disabled_date DATE,sf_id INT,sf_uploadtime DATE,sf_deviceid STRING,sf_driveid STRING,sf_state INT,sf_dest_server STRING,sf_companyid INT,sf_hardware_manufacturer STRING,sf_hardware_model STRING,sf_hardware_bootloader STRING,sf_hardware_build STRING,sf_hardware_carrier STRING,sf_android_fw_version STRING,sf_android_api_version STRING,sf_android_codename STRING,sf_android_baseband STRING,sf_raw_hardware_string STRING,sf_raw_os_string STRING,sf_utc_offset_with_dst STRING,sf_app_version STRING,sf_file_format STRING,sf_start_reason STRING,sf_stop_reason STRING,sf_previous_driveid STRING,sf_userid STRING,sf_tag_mac_address STRING,sf_tag_trip_number STRING,sf_primary_driver_app_user_id STRING,sf_tag_last_connection_number STRING,sf_gps_points_lsh_key_1 STRING,sf_gps_points_lsh_key_2 STRING,sf_gps_points_lsh_key_3 STRING,sf_hidden_by_support STRING',
                'USER' : 'mdindex',
                'HOSTS' : ['istc2.csail.mit.edu', 'istc5.csail.mit.edu', 'istc6.csail.mit.edu', 'istc7.csail.mit.edu', 'istc8.csail.mit.edu', 'istc9.csail.mit.edu', 'istc10.csail.mit.edu', 'istc11.csail.mit.edu', 'istc12.csail.mit.edu', 'istc13.csail.mit.edu'],
                'ROLEDEFS' : { 'master': ['istc2.csail.mit.edu'] },
                },
        "local_spark_join_tpch" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "spark_join_tpch" : {
                'JAR' : '/home/mdindex/yilu/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/home/mdindex/yilu/mdindex/conf/tpch.properties',
                'HOMEDIR' : '/home/mdindex/',
                'HADOOPBIN' : '/home/mdindex/hadoop-2.6.0/bin/',
                'USER' : 'mdindex',
                'HOSTS' : ['istc2.csail.mit.edu', 'istc5.csail.mit.edu', 'istc6.csail.mit.edu', 'istc7.csail.mit.edu', 'istc8.csail.mit.edu', 'istc9.csail.mit.edu', 'istc10.csail.mit.edu', 'istc11.csail.mit.edu', 'istc12.csail.mit.edu', 'istc13.csail.mit.edu'],
                'ROLEDEFS' : { 'master': ['istc2.csail.mit.edu'] },
                },
        "join_tpch": {
                'JAR' : '/home/mdindex/yilu/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/home/mdindex/yilu/mdindex/conf/tpch.properties',
                'HOMEDIR' : '/home/mdindex/',
                'HADOOPBIN' : '/home/mdindex/hadoop-2.6.0/bin/',
                'SCHEMALINEITEM': 'l_orderkey int, l_partkey int, l_suppkey int, l_linenumber int, l_quantity double, l_extendedprice double, l_discount double, l_tax double, l_returnflag string,  l_linestatus string, l_shipdate date, l_commitdate date, l_receiptdate date, l_shipinstruct string, l_shipmode string',
                'SCHEMAORDERS': 'o_orderkey int, o_custkey int, o_orderstatus string, o_totalprice double, o_orderdate date, o_orderpriority string, o_clerk string, o_shippriority int',
                'SCHEMAPART': 'p_partkey int, p_name string, p_mfgr string, p_brand string, p_type string, p_size int, p_container string, p_retailprice double',
                'SCHEMASUPPLIER': 's_suppkey int, s_name string, s_address string, s_phone string, s_acctbal double, s_nation string, s_region string',
                'SCHEMACUSTOMER': 'c_custkey int, c_name string, c_address string, c_phone string, c_acctbal double, c_mktsegment string, c_nation string, c_region string',
                'USER' : 'mdindex',
                'HOSTS' : ['istc2.csail.mit.edu', 'istc5.csail.mit.edu', 'istc6.csail.mit.edu', 'istc7.csail.mit.edu', 'istc8.csail.mit.edu', 'istc9.csail.mit.edu', 'istc10.csail.mit.edu', 'istc11.csail.mit.edu', 'istc12.csail.mit.edu', 'istc13.csail.mit.edu'],
                'ROLEDEFS' : { 'master': ['istc2.csail.mit.edu'] },
                },
        "join_lineitem" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/tpchdata/lineitem',
                'TABLENAME' : 'lineitem',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.1',
                'DELIMITER': '|',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '6001215',
                'NUMFIELDS' : '15',
                'SCHEMA': 'l_orderkey int, l_partkey int, l_suppkey int, l_linenumber int, l_quantity double, l_extendedprice double, l_discount double, l_tax double, l_returnflag string,  l_linestatus string, l_shipdate date, l_commitdate date, l_receiptdate date, l_shipinstruct string, l_shipmode string',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "join_orders" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/tpchdata/orders',
                'TABLENAME' : 'orders',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.1',
                'DELIMITER': '|',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '1500000',
                'NUMFIELDS' : '8',
                'SCHEMA': 'o_orderkey int, o_custkey int, o_orderstatus string, o_totalprice double, o_orderdate date, o_orderpriority string, o_clerk string, o_shippriority int',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "join_part" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/tpchdata/part',
                'TABLENAME' : 'part',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.5',
                'DELIMITER': '|',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '200000',
                'NUMFIELDS' : '16',
                'SCHEMA': 'p_partkey int, p_name string, p_mfgr string, p_brand string, p_type string, p_size int, p_container string, p_retailprice double',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "join_supplier" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/tpchdata/supplier',
                'TABLENAME' : 'supplier',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.5',
                'DELIMITER': '|',
                'NUMBUCKETS' : '8',
                'NUMTUPLES': '10000',
                'NUMFIELDS' : '7',
                'SCHEMA': 's_suppkey int, s_name string, s_address string, s_phone string, s_acctbal double, s_nation string, s_region string',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "join_customer" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/tpchdata/customer',
                'TABLENAME' : 'customer',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.5',
                'DELIMITER': '|',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '150000',
                'NUMFIELDS' : '8',
                'SCHEMA': 'c_custkey int, c_name string, c_address string, c_phone string, c_acctbal double, c_mktsegment string, c_nation string, c_region string',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "join_cmt": {
                'JAR' : '/home/mdindex/yilu/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/home/mdindex/yilu/mdindex/conf/tpch.properties',
                'HOMEDIR' : '/home/mdindex/',
                'HADOOPBIN' : '/home/mdindex/hadoop-2.6.0/bin/',
                'SCHEMAMH' : 'mh_id INT,mh_dataset_id STRING,mh_uploadtime DATE,mh_runtime STRING,mh_trip_start DATE,mh_data_count_minutes STRING,mh_data_count_accel_samples STRING,mh_data_count_netloc_samples STRING,mh_data_count_gps_samples STRING,mh_observed_sample_rate STRING,mh_distance_mapmatched_km STRING,mh_distance_gps_km STRING,mh_ground_truth_present STRING,mh_timing_mapmatch DOUBLE,mh_distance_pct_path_error STRING,mh_build_version STRING,mh_timing_queue_wait DOUBLE,mh_data_trip_length STRING,mh_battery_maximum_level STRING,mh_battery_minimum_level STRING,mh_battery_drain_rate_per_hour STRING,mh_battery_plugged_duration_hours STRING,mh_battery_delay_from_drive_end_seconds STRING,mh_startlat STRING,mh_startlon STRING,mh_endlat STRING,mh_endlon STRING,mh_data_count_output_gps_speeding_points STRING,mh_speeding_slow_gps_points STRING,mh_speeding_10kmh_gps_points STRING,mh_speeding_20kmh_gps_points STRING,mh_speeding_40kmh_gps_points STRING,mh_speeding_80kmh_gps_points STRING,mh_output_accel_valid_minutes STRING,mh_output_gps_moving_minutes STRING,mh_output_gps_moving_and_accel_valid_minutes STRING,mh_data_time_till_first_gps_minutes STRING,mh_score_di_accel STRING,mh_score_di_brake STRING,mh_score_di_turn STRING,mh_score_di_car_motion STRING,mh_score_di_phone_motion STRING,mh_score_di_speeding STRING,mh_score_di_night STRING,mh_star_rating STRING,mh_trip_end DATE,mh_score_di_car_motion_with_accel STRING,mh_score_di_car_motion_with_speeding STRING,mh_score_di_distance_km_with_accel STRING,mh_score_di_distance_km_with_speeding STRING,mh_score_accel_per_sec_ntile STRING,mh_score_brake_per_sec_ntile STRING,mh_score_turn_per_sec_ntile STRING,mh_score_speeding_per_sec_ntile STRING,mh_score_phone_motion_per_sec_ntile STRING,mh_score_accel_per_km_ntile STRING,mh_score_brake_per_km_ntile STRING,mh_score_turn_per_km_ntile STRING,mh_score_speeding_per_km_ntile STRING,mh_score_phone_motion_per_km_ntile STRING,mh_score STRING,mh_distance_prepended_km STRING,mh_recording_start DATE,mh_score_di_distance_km STRING,mh_recording_end DATE,mh_recording_startlat STRING,mh_recording_startlon STRING,mh_display_distance_km STRING,mh_display_trip_start DATE,mh_display_startlat STRING,mh_display_startlon STRING,mh_data_count_gyro_samples STRING,mh_star_rating_accel STRING,mh_star_rating_brake STRING,mh_star_rating_turn STRING,mh_star_rating_speeding STRING,mh_star_rating_phone_motion STRING,mh_is_night STRING,mh_battery_total_drain STRING,mh_battery_total_drain_duration_hours STRING,mh_score_smoothness STRING,mh_score_awareness STRING,mh_star_rating_night STRING,mh_star_rating_smoothness STRING,mh_star_rating_awareness STRING,mh_hide STRING,mh_data_count_tag_accel_samples STRING,mh_quat_i STRING,mh_quat_j STRING,mh_quat_k STRING,mh_quat_r STRING,mh_passenger_star_rating STRING,mh_suspension_damping_ratio STRING,mh_suspension_natural_frequency STRING,mh_suspension_fit_error STRING,mh_driving STRING,mh_trip_mode STRING,mh_classification_confidence STRING,mh_gk_trip_mode STRING,mh_gk_confidence STRING,mh_offroad_trip_mode STRING,mh_offroad_confidence STRING,mh_driver_confidence STRING,mh_timing_processing_preprocessing DOUBLE,mh_timing_processing_gatekeeper DOUBLE,mh_timing_processing_accelpipeline DOUBLE,mh_timing_processing_offroad DOUBLE,mh_timing_processing_suspension DOUBLE,mh_timing_processing_scoring DOUBLE,mh_timing_processing_hitchhiker DOUBLE,mh_data_count_obd_samples STRING,mh_data_count_pressure_samples STRING,mh_raw_sampling_mode STRING,mh_data_count_magnetometer_samples STRING,mh_location_disabled_date DATE',
                'SCHEMAMHL': 'mhl_dataset_id INT, mhl_mapmatch_history_id INT',
                'SCHEMASF' : 'sf_id INT,sf_uploadtime DATE,sf_deviceid STRING,sf_driveid STRING,sf_state INT,sf_dest_server STRING,sf_companyid INT,sf_hardware_manufacturer STRING,sf_hardware_model STRING,sf_hardware_bootloader STRING,sf_hardware_build STRING,sf_hardware_carrier STRING,sf_android_fw_version STRING,sf_android_api_version STRING,sf_android_codename STRING,sf_android_baseband STRING,sf_raw_hardware_string STRING,sf_raw_os_string STRING,sf_utc_offset_with_dst STRING,sf_app_version STRING,sf_file_format STRING,sf_start_reason STRING,sf_stop_reason STRING,sf_previous_driveid STRING,sf_userid STRING,sf_tag_mac_address STRING,sf_tag_trip_number STRING,sf_primary_driver_app_user_id STRING,sf_tag_last_connection_number STRING,sf_gps_points_lsh_key_1 STRING,sf_gps_points_lsh_key_2 STRING,sf_gps_points_lsh_key_3 STRING,sf_hidden_by_support STRING',
                'USER' : 'mdindex',
                'HOSTS' : ['istc2.csail.mit.edu', 'istc5.csail.mit.edu', 'istc6.csail.mit.edu', 'istc7.csail.mit.edu', 'istc8.csail.mit.edu', 'istc9.csail.mit.edu', 'istc10.csail.mit.edu', 'istc11.csail.mit.edu', 'istc12.csail.mit.edu', 'istc13.csail.mit.edu'],
                'ROLEDEFS' : { 'master': ['istc2.csail.mit.edu'] },
                },
        "join_mh" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/cmtdata/mh',
                'TABLENAME' : 'mh',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.1',
                'DELIMITER': ';',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '100000',
                'NUMFIELDS' : '115',
                'SCHEMA' : 'mh_id INT,mh_dataset_id STRING,mh_uploadtime DATE,mh_runtime STRING,mh_trip_start DATE,mh_data_count_minutes STRING,mh_data_count_accel_samples STRING,mh_data_count_netloc_samples STRING,mh_data_count_gps_samples STRING,mh_observed_sample_rate STRING,mh_distance_mapmatched_km STRING,mh_distance_gps_km STRING,mh_ground_truth_present STRING,mh_timing_mapmatch DOUBLE,mh_distance_pct_path_error STRING,mh_build_version STRING,mh_timing_queue_wait DOUBLE,mh_data_trip_length STRING,mh_battery_maximum_level STRING,mh_battery_minimum_level STRING,mh_battery_drain_rate_per_hour STRING,mh_battery_plugged_duration_hours STRING,mh_battery_delay_from_drive_end_seconds STRING,mh_startlat STRING,mh_startlon STRING,mh_endlat STRING,mh_endlon STRING,mh_data_count_output_gps_speeding_points STRING,mh_speeding_slow_gps_points STRING,mh_speeding_10kmh_gps_points STRING,mh_speeding_20kmh_gps_points STRING,mh_speeding_40kmh_gps_points STRING,mh_speeding_80kmh_gps_points STRING,mh_output_accel_valid_minutes STRING,mh_output_gps_moving_minutes STRING,mh_output_gps_moving_and_accel_valid_minutes STRING,mh_data_time_till_first_gps_minutes STRING,mh_score_di_accel STRING,mh_score_di_brake STRING,mh_score_di_turn STRING,mh_score_di_car_motion STRING,mh_score_di_phone_motion STRING,mh_score_di_speeding STRING,mh_score_di_night STRING,mh_star_rating STRING,mh_trip_end DATE,mh_score_di_car_motion_with_accel STRING,mh_score_di_car_motion_with_speeding STRING,mh_score_di_distance_km_with_accel STRING,mh_score_di_distance_km_with_speeding STRING,mh_score_accel_per_sec_ntile STRING,mh_score_brake_per_sec_ntile STRING,mh_score_turn_per_sec_ntile STRING,mh_score_speeding_per_sec_ntile STRING,mh_score_phone_motion_per_sec_ntile STRING,mh_score_accel_per_km_ntile STRING,mh_score_brake_per_km_ntile STRING,mh_score_turn_per_km_ntile STRING,mh_score_speeding_per_km_ntile STRING,mh_score_phone_motion_per_km_ntile STRING,mh_score STRING,mh_distance_prepended_km STRING,mh_recording_start DATE,mh_score_di_distance_km STRING,mh_recording_end DATE,mh_recording_startlat STRING,mh_recording_startlon STRING,mh_display_distance_km STRING,mh_display_trip_start DATE,mh_display_startlat STRING,mh_display_startlon STRING,mh_data_count_gyro_samples STRING,mh_star_rating_accel STRING,mh_star_rating_brake STRING,mh_star_rating_turn STRING,mh_star_rating_speeding STRING,mh_star_rating_phone_motion STRING,mh_is_night STRING,mh_battery_total_drain STRING,mh_battery_total_drain_duration_hours STRING,mh_score_smoothness STRING,mh_score_awareness STRING,mh_star_rating_night STRING,mh_star_rating_smoothness STRING,mh_star_rating_awareness STRING,mh_hide STRING,mh_data_count_tag_accel_samples STRING,mh_quat_i STRING,mh_quat_j STRING,mh_quat_k STRING,mh_quat_r STRING,mh_passenger_star_rating STRING,mh_suspension_damping_ratio STRING,mh_suspension_natural_frequency STRING,mh_suspension_fit_error STRING,mh_driving STRING,mh_trip_mode STRING,mh_classification_confidence STRING,mh_gk_trip_mode STRING,mh_gk_confidence STRING,mh_offroad_trip_mode STRING,mh_offroad_confidence STRING,mh_driver_confidence STRING,mh_timing_processing_preprocessing DOUBLE,mh_timing_processing_gatekeeper DOUBLE,mh_timing_processing_accelpipeline DOUBLE,mh_timing_processing_offroad DOUBLE,mh_timing_processing_suspension DOUBLE,mh_timing_processing_scoring DOUBLE,mh_timing_processing_hitchhiker DOUBLE,mh_data_count_obd_samples STRING,mh_data_count_pressure_samples STRING,mh_raw_sampling_mode STRING,mh_data_count_magnetometer_samples STRING,mh_location_disabled_date DATE',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "join_mhl" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/cmtdata/mhl',
                'TABLENAME' : 'mhl',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.1',
                'DELIMITER': ';',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '100000',
                'NUMFIELDS' : '2',
                'SCHEMA' : 'mhl_dataset_id INT, mhl_mapmatch_history_id INT',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                },
        "join_sf" : {
                'JAR' : '/Users/ylu/Documents/workspace/mdindex/build/libs/mdindex-all.jar',
                'CONF' : '/Users/ylu/Documents/workspace/mdindex/conf/ylu.properties',
                'INPUTSDIR' : '/Users/ylu/Documents/workspace/cmtdata/sf',
                'TABLENAME' : 'sf',
                'HDFSDIR' : '/user/ylu',
                'HOMEDIR' : '/Users/ylu',
                'HADOOPBIN' : '/Users/ylu/Documents/workspace/hadoop-2.6.0/bin',
                'SAMPLINGRATE' : '0.1',
                'DELIMITER': ';',
                'NUMBUCKETS' : '16',
                'NUMTUPLES': '100000',
                'NUMFIELDS' : '33',
                'SCHEMA' : 'sf_id INT,sf_uploadtime DATE,sf_deviceid STRING,sf_driveid STRING,sf_state INT,sf_dest_server STRING,sf_companyid INT,sf_hardware_manufacturer STRING,sf_hardware_model STRING,sf_hardware_bootloader STRING,sf_hardware_build STRING,sf_hardware_carrier STRING,sf_android_fw_version STRING,sf_android_api_version STRING,sf_android_codename STRING,sf_android_baseband STRING,sf_raw_hardware_string STRING,sf_raw_os_string STRING,sf_utc_offset_with_dst STRING,sf_app_version STRING,sf_file_format STRING,sf_start_reason STRING,sf_stop_reason STRING,sf_previous_driveid STRING,sf_userid STRING,sf_tag_mac_address STRING,sf_tag_trip_number STRING,sf_primary_driver_app_user_id STRING,sf_tag_last_connection_number STRING,sf_gps_points_lsh_key_1 STRING,sf_gps_points_lsh_key_2 STRING,sf_gps_points_lsh_key_3 STRING,sf_hidden_by_support STRING',
                'USER': 'ylu',
                'HOSTS': ['localhost'],
                'ROLEDEFS': { 'master': ['localhost'] }
                }
        }
