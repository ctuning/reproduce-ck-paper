ck rm experiment:reproduce-ck-paper-autotune-flags-susan-linux-pareto
ck cp experiment:reproduce-ck-paper-autotune-flags-susan-linux-i10 :reproduce-ck-paper-autotune-flags-susan-linux-pareto
ck autotune pipeline:program pipeline_from_file=_setup_program_pipeline_tmp.json @autotune_program_pipeline_i10_apply_pareto.json
