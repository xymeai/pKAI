clear-dist:
    rm -rf ./dist

package: clear-dist
    uv build

publish: package
    uv publish --index xyme-pypi --username "test"

# Format the code
format:
    ruff format

# Check whether the code is formatted
format-check:
    ruff format --check

# Lint the code for syntactic errors
lint:
    pyright