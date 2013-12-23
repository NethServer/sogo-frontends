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

DESTDIR ?= root/usr/share/nethesis/sogo-frontends
TEMPLATEDIR ?= root/etc/e-smith/templates/sogo-frontends
XPILIST := $(shell cut -f 3 -d ' ' < SHA1SUM)

# xpi download mirrors. Try local host at first to save bandwidth:
XPIMIRRORS += $(shell echo http://`hostname`/nethserver/sogo-frontends)
XPIMIRRORS += $(shell echo http://`hostname`/sogo-thunderbird/frontends)
XPIMIRRORS += http://dev.nethesis.it/nethserver/sogo-frontends
XPIMIRRORS += http://www.sogo.nu/files/downloads/extensions

.PHONY: download check clean install

download: $(XPILIST)

check: SHA1SUM
	sha1sum -c SHA1SUM

clean:
	@rm -fv $(XPILIST)

%.xpi:
	@echo "Downloading $@...";
	@for M in $(XPIMIRRORS); do \
		echo "Trying $$M/$@"; \
		curl -k -L -s -S -f -O $$M/$@ && echo "OK" && exit 0 ;\
	done; \
	echo "FAILED."; \
	exit 1

install:
	@echo "Installing..."
	install -d $(DESTDIR) $(TEMPLATEDIR)
	install -m 0644 *.xpi $(DESTDIR)
	install -m 0644 MANIFEST* $(DESTDIR)
	install -m 0644 *.patch $(TEMPLATEDIR)

