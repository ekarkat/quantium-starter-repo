#!/bin/bash

# Activate the virtual environment
source /home/honk/portfolio/dash/bin/activate

# Execute the test suite
pytest /home/honk/portfolio/quantium-starter-repo/test_dashapp.py

# Capture the status of the pytest execution
status=$?

# Deactivate the virtual environment
deactivate

# Check if tests passed and return appropriate exit code
if [ $status -eq 0 ]
then
    echo "Tests passed successfully."
    exit 0
else
    echo "Tests failed."
    exit 1
fi
