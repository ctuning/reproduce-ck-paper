call ck rm experiment:reproduce-ck-paper-autotune-flags-susan-android-pareto
call ck cp experiment:reproduce-ck-paper-autotune-flags-susan-android-i10 :reproduce-ck-paper-autotune-flags-susan-android-pareto
call ck autotune pipeline:program pipeline_from_file=_setup_program_pipeline_tmp.json @autotune_program_pipeline_i10_apply_pareto.json
