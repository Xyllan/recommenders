def load_modules():
    import os
    libs = os.path.abspath(os.path.join('..', '..'))
    import sys
    if libs not in sys.path:
        sys.path.append(libs)