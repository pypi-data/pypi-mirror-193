# __version__ will be set by the github workflow at .github/workflows/python-release.yml
import sys
from pathlib import Path
# TODO (2021/11) this is a workaround. To function as a package, all imports need to be done from the source root,
#   i.e. valuation -> 'from valuation.ql import QLObjectDB' instead of 'from ql import QLObjectDB'
#   see https://scdm-financial.atlassian.net/jira/software/projects/OP/boards/48/backlog?selectedIssue=OP-63
sys.path.append(str(Path(__file__).parent))
