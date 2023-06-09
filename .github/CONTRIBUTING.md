# Contributing to RISC
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## We Develop with Github
We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## We Use [GitHub Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from the **`dev` branch**.
2. If you've added code that should be tested, you **must** ensure it is properly tested.
3. If you've changed APIs, update the in-code documentation.
4. Ensure the CI/CD test suite passes.
5. Make sure your code lints.
6. Submit that pull request!

## Any contributions you make will be under the LGPLv3 Software License
In short, when you submit code changes, your submissions are understood to be under the same [LGPLv3 License](https://choosealicense.com/licenses/lgpl-3.0/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Write bug reports with detail, background, and sample code

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/GRAAL-Research/risc/issues). You should use one of our [proposed templates](https://github.com/GRAAL-Research/risc/tree/main/.github/ISSUE_TEMPLATE) when appropriate; they are integrated with GitHub and do most of the formatting for you. It's that easy!

**Great Bug Reports** tend to have:

- A quick and clear summary and/or background
- Steps to reproduce
  - Be specific and clear!
  - Give sample code if you can. Try to reduce the bug to the minimum amount of code needed to reproduce: it will help in our troubleshooting procedure.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)
Feel free to include any print screen or other file you feel may further clarify your point.

## Do you have a suggestion for an enhancement?

We use GitHub issues to track enhancement requests.  Before you create an enhancement request:

* Make sure you have a clear idea of the enhancement you would like.  If you have a vague idea, consider discussing
it first on the users list.

* Check the in-code documentation to make sure your feature does not already exist.

* Do a [quick search](https://github.com/GRAAL-Research/risc/issues) to see whether your enhancement has already been suggested.

When creating your enhancement request, please:

* Provide a clear title and description.

* Explain why the enhancement would be useful.  It may be helpful to highlight the feature in other libraries.

* Include code examples to demonstrate how the enhancement would be used.


## Prerequisites

We created three requirements files to install all the tools used for the development of the library. `tests/requirements.txt` define the requirements for the tests.

You can install all the requirements with

``` shell
pip install -r tests/requirements.txt
pip install -r styling_requirements.txt
```

Also, you should run `python setup.py develop` to build the project.
``` shell
python setup.py develop
```

## Use a Consistent Coding Style

All of the code is formatted using [black](https://black.readthedocs.io) with the associated [config file](https://github.com/GRAAL-Research/risc/blob/main/pyproject.toml). In order to format the code of your submission, simply run
> See the [styling requirements](https://github.com/GRAAL-Research/risc/blob/main/styling_requirements.txt) for the proper black version to use.

``` shell
black .
```

We also have our own `pylint` [config file](https://github.com/GRAAL-Research/risc/blob/main/.pylintrc). Try not to introduce code incoherences detected by the linting. You can run the linting procedure with
> See the [styling requirements](https://github.com/GRAAL-Research/risc/blob/main/styling_requirements.txt) for the proper pylint version to use.

``` shell
pylint risc
pylint tests
```

## Tests

If your pull request introduces a new feature, please deliver it with tests that ensure correct behavior. All of the current tests are located under the `tests` folder, if you want to see some examples.

For any pull request submitted, **ALL** of the tests must succeed. You can run the tests with

``` shell
pytest

# or with multiple CPU

pytest -n 4
```

> The integration tests need to be executed on a device with a GPU.

We also provide a script, `run_tests_python_envs.sh`, to run all the tests in all the supported versions. To do so, you need to install Conda and run
the following command

``` shell
bash -l run_tests_python_envs.sh # For bash terminal
zsh -i run_tests_python_envs.sh # For ZSH terminal
```

## Documentation

When submitting a pull request for a new feature, try to include in-code documentation for the new objects/modules introduced and their public methods.

## License
By contributing, you agree that your contributions will be licensed under its LGPLv3 License.

## References
This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md).
