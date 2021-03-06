# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Maskave

def test_Maskave_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-2,
    ),
    mask=dict(argstr='-mask %s',
    position=1,
    ),
    out_file=dict(argstr='> %s',
    keep_extension=True,
    name_source='in_file',
    name_template='%s_maskave.1D',
    position=-1,
    ),
    outputtype=dict(),
    quiet=dict(argstr='-quiet',
    position=2,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = Maskave.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Maskave_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Maskave.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

