import os
import argparse
from pathlib import Path
import json
from valuation.olympia.excel_templates.instruments import write_instruments
from valuation.olympia.excel_templates.non_instruments import write_non_instrument
from valuation.olympia.input.config import write_empty_config
from daa_utils import safe_makedir, input_output_pairs, zip_files


def make_excel_templates(out_base: str, template_version: str, no_test: bool = True) -> None:
    extension = 'xlsx' if no_test else 'csv'
    instruments = os.path.join(out_base, 'InstrumentTemplates')
    non_instrument = os.path.join(out_base, 'MarketDataAndProcessTemplates')
    defaults = os.path.join(out_base, 'ValuationConfiguration')
    safe_makedir(instruments)
    safe_makedir(non_instrument)
    safe_makedir(defaults)
    defaults_base_path = defaults if no_test else None
    olympia_defaults_base = os.path.join(Path(os.path.dirname(__file__)).parent, 'input', 'defaults')
    in_out_pairs = input_output_pairs(olympia_defaults_base, defaults, '*.json', extension='json')
    for in_file, out_file, _ in in_out_pairs:
        with open(in_file, mode='r') as in_handle:
            content = json.load(in_handle)
        with open(out_file, mode='w') as out_handle:
            json.dump(content, out_handle, indent=4)
    write_instruments(instruments, template_version, extension=extension)
    write_non_instrument(non_instrument, extension=extension)
    write_empty_config(out_base, template_version, defaults_base_path=defaults_base_path)


def release_templates(template_version: str) -> None:
    out_base = os.path.join(os.path.dirname(__file__), 'releases', f'templates_{template_version}')
    safe_makedir(out_base)
    make_excel_templates(out_base, template_version)
    zip_files(out_base, delete_after_packing=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Template generation')
    parser.add_argument('version', type=str)
    args = parser.parse_args()
    release_templates(args.version)
