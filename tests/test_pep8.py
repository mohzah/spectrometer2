import pep8


def test_pep8_conformance():
    """Test that we conform to PEP8."""
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['./spectrometer/githelpers.py',
                                    './spectrometer/dashboard/views.py'])
    print(result.counters)
    if result.counters.get('E902', False):
        print('Could not find/open one of files')
    assert result.total_errors == 0
