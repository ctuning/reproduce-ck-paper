ck rm experiment:demo-autotune-flags-susan-odroid-0-3-pareto
ck cp experiment:demo-autotune-flags-susan-odroid-0-3-i10 :demo-autotune-flags-susan-odroid-0-3-pareto
ck autotune pipeline:program pipeline_from_file=_setup_program_pipeline_tmp.json @autotune_program_pipeline_i10_apply_pareto.json
