from setuptools import Extension, setup

setup(
	ext_modules=[
		Extension(
			name="spam",
			sources=["spammodule.c"],
		),
	]
)
