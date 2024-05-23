import os

# Create a directory structure for a trading project
# Directories: src/config, src/data, src/spark, src/strategies, src/analysis, src/ranking, src/execution, src/pnl, src/utils, tests, config, scripts, data/raw, notebooks
# Files: README.md, requirements.txt, setup.py, config/config.yaml, scripts/run_all.sh
# Files in src: config/settings.py, data/download_data.py, spark/spark_job.py, spark/spark_utils.py, strategies/strategy1.py, analysis/analyze_data.py, ranking/rank_strategies.py, execution/execute_trades.py, pnl/calculate_pnl.py, utils/common_utils.py
# Test files: tests/test_data.py, tests/test_strategies.py, tests/test_analysis.py, tests/test_ranking.py, tests/test_execution.py, tests/test_pnl.py, tests/test_spark.py
# Notebook: notebooks/analysis_notebook.ipynb
# Create directories
directories = [
    'src/config',
    'src/data',
    'src/spark',
    'src/strategies',
    'src/analysis',
    'src/ranking',
    'src/execution',
    'src/pnl',
    'src/utils',
    'tests',
    'config',
    'scripts',
    'data/raw',
    'notebooks'
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files
files = [
    'README.md',
    'requirements.txt',
    'setup.py',
    'config/config.yaml',
    'scripts/run_all.sh'
]

for file in files:
    open(file, 'w').close()

# Create files in src directory
src_files = [
    'config/settings.py',
    'data/download_data.py',
    'spark/spark_job.py',
    'spark/spark_utils.py',
    'strategies/strategy1.py',
    'analysis/analyze_data.py',
    'ranking/rank_strategies.py',
    'execution/execute_trades.py',
    'pnl/calculate_pnl.py',
    'utils/common_utils.py'
]

for file in src_files:
    open('src/' + file, 'w').close()

# Create test files
test_files = [
    'tests/test_data.py',
    'tests/test_strategies.py',
    'tests/test_analysis.py',
    'tests/test_ranking.py',
    'tests/test_execution.py',
    'tests/test_pnl.py',
    'tests/test_spark.py'
]

for file in test_files:
    open(file, 'w').close()

# Create notebook
open('notebooks/analysis_notebook.ipynb', 'w').close()