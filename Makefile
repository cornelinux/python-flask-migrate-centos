VERSION=1.5.1
clean:
	rm -f v${VERSION}.zip
	rm -fr RHBUILD
	rm -fr Flask-Migrate-${VERSION}
centos:
	make clean
	wget https://github.com/miguelgrinberg/Flask-Migrate/archive/v${VERSION}.zip
	mkdir -p RHBUILD/BUILD
	mkdir -p RHBUILD/RPMS
	mkdir -p RHBUILD/SOURCES
	unzip v${VERSION}.zip
	mv Flask-Migrate-${VERSION} RHBUILD/SOURCES/python-flask-migrate-${VERSION}
	(cd RHBUILD/SOURCES; tar -zcf python-flask-migrate-${VERSION}.tar.gz python-flask-migrate-${VERSION})
	rpmbuild --define "_topdir $(CURDIR)/RHBUILD" -ba python-flask-migrate.spec
	
