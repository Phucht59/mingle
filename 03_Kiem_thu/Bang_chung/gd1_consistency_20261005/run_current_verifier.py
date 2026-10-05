"""Execute unchanged current verifier; redirect its sole report to append-only audit evidence."""
import importlib.util
from pathlib import Path
import sys
import argparse
R=Path('C:/Mingo')
E=R/'03_Kiem_thu/Bang_chung/gd1_consistency_20261005'
parser=argparse.ArgumentParser()
parser.add_argument('--output',default='current_candidate_verification_before.json')
args=parser.parse_args()
if Path(args.output).name!=args.output or not args.output.endswith('.json'):
    raise ValueError('Output must be an audit JSON filename')
p=R/'04_Van_hanh/Scripts/verify_evidence_gated_phase2.py'
spec=importlib.util.spec_from_file_location('gd1_existing_current_verifier',p)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
original=Path.write_text
expected=R/'03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/CURRENT_CANDIDATE_VERIFICATION.json'
def redirect(self,*args,**kwargs):
    if self.resolve()!=expected.resolve():
        raise RuntimeError('Unexpected verifier write: '+str(self))
    return original(E/parsed_output,*args,**kwargs)
parsed_output=args.output
Path.write_text=redirect
try:
    result=m.run()
finally:
    Path.write_text=original
sys.exit(result)
