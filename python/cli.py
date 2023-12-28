import argparse
import sys


MISSING_DOCUMENTATION = (
    "[HELP MISSING] Help text for this command/option is missing. Help out by making a "
    "pull request at: github.com/clinical-Genomics-Lund/bnf-infrastructure/"
)


def cli_parser():

    parser = argparse.ArgumentParser(
        description="Use/add/modify the data in the coyote database!",
        epilog="Show help for each subcommand with import_coyote_sample.py {subcommand} -h",
    )

    subparsers = parser.add_subparsers(dest="command_selection")
    base_subparser = argparse.ArgumentParser(add_help=False)

    """
    GLOBAL COMMANDS
    """
    base_subparser.add_argument(
        "--debug",
        action="store_true",
        dest="debug_logger",
        default=False,
        help="Print debug information to STDOUT.",
    )

    base_subparser.add_argument(
        "-q",
        "--quiet",
        default=False,
        action="store_true",
        help="When loading via CRON jobs hide output",
    )

    """
    MAIN COMMANDS
    """

    usage_msg = "For usage examples, see: http://mtlucmds1.lund.skane.se/wiki/doku.php?id=coyote"

    load = subparsers.add_parser(
        "load",
        parents=[base_subparser],
        description="Load case into coyote, flag for each datatype",
        help="Load case into coyote, flag for each datatype",
        epilog=usage_msg,
    )
    yaml = subparsers.add_parser(
        "yaml",
        parents=[base_subparser],
        description="Load case into coyote, all input defined in yaml-format",
        help="Load case into coyote, all input defined in yaml-format",
        epilog=usage_msg,
    )

    """
    YAML Custom args
    """
    yaml.add_argument(
        "-y",
        "--yaml",
        dest="yaml_file",
        required=True,
        help="Path to YAML file with all sample meta info and relevant VCFs JSONs and BED files to load",
    )
    yaml.add_argument(
        "--increment",
        dest="increment",
        default=True,
        help="If case ID already exists, increment this case by number of matches + 1",
    )

    """
    LOAD Custom args
    """
    load.add_argument(
        "-v",
        "--vcf",
        dest="vcf",
        required=True,
        help="Path to SNV VCF, VEP annotated. Preferred SomaticPanelPipeline annotation for maximum usage",
    )
    load.add_argument(
        "--id",
        dest="name",
        required=True,
        help="Case ID, name of case in coyote. Related flags --increment",
    )
    load.add_argument(
        "--group",
        dest="groups",
        required=True,
        help="Group name of case, to which group of coyote does sample belong. Example: myeloid_GMSv1.0",
    )
    load.add_argument(
        "--clarity-sample-id",
        dest="clarity-sample-id",
        help="Clarity Sample ID, need to make clarity db matches",
    )
    load.add_argument(
        "--clarity-pool-id",
        dest="clarity-pool-id",
        help="Of which pool was this sample part of",
    )
    load.add_argument(
        "--gens",
        dest="gens_id",
        help="ID of this case in GENS cmdscout2.lund.skane.se/gens",
    )
    load.add_argument(
        "--subpanel",
        dest="subpanel",
        help="Is this sample subcategorized into a smaller panel? Example for solid_GMSv3.0: ovarian|solid|breast|cns|lungthyroid",
    )
    load.add_argument(
        "--purity",
        dest="purity",
        help="Tumour purity of sample",
    )
    load.add_argument(
        "--build",
        dest="build",
        required=True,
        help="To which genome build is the case aligned to",
    )
    load.add_argument(
        "--increment",
        dest="increment",
        default=True,
        help="If case ID already exists, increment this case by number of matches + 1",
    )
    load.add_argument(
        "--cnv",
        dest="cnv",
        help="Path to CNV JSON, required output from SomaticPanelPipeline",
    )
    load.add_argument(
        "--transloc",
        dest="transloc",
        help="Path to SNPeff annotated DNA translocations",
    )
    load.add_argument(
        "--lowcov",
        dest="lowcov",
        help="Path to annotated BED file with average read depths",
    )
    load.add_argument(
        "--biomarkers",
        dest="biomarkers",
        help="Path to biomarkers JSON",
    )
    load.add_argument(
        "--cnvprofile",
        dest="cnvprofile",
        help="Path to cnvprofile image",
    )
    load.add_argument(
        "--fusions",
        dest="fusions",
        help="Path to fusions JSON",
    )

#GetOptions( \%opt, 'vcf=s', 'id=s', 'clarity-sample-id=s', 'clarity-pool-id=s', 'bam=s', 'group=s', 'cnv=s', 'transloc=s', 'qc=s', 'cnvprofile=s', 'build=s', 'gens=s', 'biomarkers=s', 'subpanel=s', 'purity=s', 'lowcov=s' );








    return parser
