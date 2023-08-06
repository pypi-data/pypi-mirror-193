import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def _get_version() -> str:
    with open("src/valuation/__init__.py", encoding='utf-8') as file_handle:
        lines = file_handle.read().split('\n')
    for line in lines:
        if line.startswith('__version__'):
            return line[line.find("'") + 1:-1]
    return 'v0.0.1'  # no version defined in __init__


setuptools.setup(
    name="valuation",
    version='0.1.7',
    author="Deloitte Audit Analytics GmbH | Valuation",
    author_email="daa-valuation@deloitte-audit-analytics.com",
    description="Financial Valuation Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Deloitte-Audit-Analytics/DaaValuationEngine",
    project_urls={
        "Bug Tracker": "https://scdm-financial.atlassian.net/jira/software/projects/OP/boards/48/backlog",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        # If any package contains *.ini files, include them
        '': ['*.ini', '*.csv'],
    },
    packages=setuptools.find_packages(where="src", exclude=('cloud_functions', 'pricing_service')),
    python_requires=">=3.9",
)
