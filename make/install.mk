install: ${VERSION}
	@pip install \
		--extra-index-url https://software.siemens.dk/pypi/ \
		--trusted-host software.siemens.dk \
		-e .

install-production: ${VERSION}
	@pip install \
		--extra-index-url https://software.siemens.dk/pypi/ \
		--trusted-host software.siemens.dk .

install-all: ${VERSION}
	@pip install \
		--extra-index-url https://software.siemens.dk/pypi/ \
		--trusted-host software.siemens.dk \
		-e '.[all]'

install-dev: ${VERSION}
	@pip install \
		--extra-index-url https://software.siemens.dk/pypi/ \
		--trusted-host software.siemens.dk \
		-e '.[dev]'

install-tests: ${VERSION}
	@pip install \
		--extra-index-url https://software.siemens.dk/pypi/ \
		--trusted-host software.siemens.dk \
		-e '.[tests]'
