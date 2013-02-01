#
# sogo-frontends Makefile
#
# Download and check integrity of a bundle of XPI files. The file list
# is declared in SHA1SUM file.
#
# Typical usage:
#
# 1. Check SOGOURL variable correctness
# 2.   $ make download
# 3.   $ make check
#
# If you need to add new XPIs:
#
# 1. Download the new XPI
# 2. Add the sha1 signature to SHA1SUM file  -- see sha1sum(1) manpage
#

#
# Copyright (C) 2013 Nethesis S.r.l.
# http://www.nethesis.it - support@nethesis.it
# 
# This script is part of NethServer.
# 
# NethServer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License,
# or any later version.
# 
# NethServer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
#

SOGOURL := http://www.sogo.nu/files/downloads/extensions
XPILIST := $(shell cut -f 3 -d ' ' < SHA1SUM)

.PHONY: download check clean build-rpm build-srpm

download: $(XPILIST)

check:
	@sha1sum -c SHA1SUM

clean:
	@rm -fv $(XPILIST)

%.xpi:
	@echo "Downloading $@...";
	@curl -O $(SOGOURL)/$@	

build-rpm: build-srpm


build-srpm: download check
	mock
