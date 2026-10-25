# Beta (0.0.1)
The initial functionalities of simulation for automobile insurance contracts for FR and EN.

# 0.0.2
- Fixed error in a title of the generated text.

# 0.0.3
- Fix model filename and loading path.
- Release of new V2 model and delete of V1 model.



# 0.1.0
- Support Python 3.11, 3.12, 3.13 and 3.14; drop Python 3.8, 3.9 and 3.10.
- Support NumPy 2, pandas 2.1+ and SDV 1.14 to 1.x (SDV 2 is not supported yet).
- Fix the default TVAE model path: it pointed to the deleted `tvae_model_v1.pkl` and was passed as a tuple, and the
  model file was not shipped inside the package.
- Fix contracts sharing their language: creating a French contract after an English one switched the English
  contract text to French. Text generators are now bound per contract instead of on the `FPQ1Contract` class.
- Load the TVAE model with `sdv.utils.load_synthesizer` when available (`TVAESynthesizer.load` is deprecated).
- Add `risc_generator.__version__`.
- Move the packaging to `pyproject.toml` (PEP 621) and replace black and pylint with Ruff.
- Run the tests on Python 3.11 to 3.14 in a single CI workflow, including end-to-end tests with the pre-trained model.
