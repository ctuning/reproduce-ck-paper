ck cp experiment:reproduce-ck-paper-autotune-compiler-flags-susan-android-i100 experiment:reproduce-ck-paper-autotune-flags-susan-android-pareto
ck autotune pipeline:program pipeline_from_file=_setup_program_pipeline_tmp.json @autotune_program_pipeline_i100_apply_pareto.json
