#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pillar
Version  : 1.2.1
Release  : 7
URL      : https://cran.r-project.org/src/contrib/pillar_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pillar_1.2.1.tar.gz
Summary  : Coloured Formatting for Columns
Group    : Development/Tools
License  : GPL-3.0
Requires: R-cli
Requires: R-rlang
Requires: R-utf8
BuildRequires : R-cli
BuildRequires : R-rlang
BuildRequires : R-utf8
BuildRequires : clr-R-helpers

%description
of data using the full range of colours provided by modern terminals.

%prep
%setup -q -c -n pillar

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523420197

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523420197
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pillar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pillar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pillar
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pillar|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pillar/DESCRIPTION
/usr/lib64/R/library/pillar/INDEX
/usr/lib64/R/library/pillar/Meta/Rd.rds
/usr/lib64/R/library/pillar/Meta/features.rds
/usr/lib64/R/library/pillar/Meta/hsearch.rds
/usr/lib64/R/library/pillar/Meta/links.rds
/usr/lib64/R/library/pillar/Meta/nsInfo.rds
/usr/lib64/R/library/pillar/Meta/package.rds
/usr/lib64/R/library/pillar/NAMESPACE
/usr/lib64/R/library/pillar/NEWS.md
/usr/lib64/R/library/pillar/R/pillar
/usr/lib64/R/library/pillar/R/pillar.rdb
/usr/lib64/R/library/pillar/R/pillar.rdx
/usr/lib64/R/library/pillar/help/AnIndex
/usr/lib64/R/library/pillar/help/aliases.rds
/usr/lib64/R/library/pillar/help/figures/colours.png
/usr/lib64/R/library/pillar/help/paths.rds
/usr/lib64/R/library/pillar/help/pillar.rdb
/usr/lib64/R/library/pillar/help/pillar.rdx
/usr/lib64/R/library/pillar/html/00Index.html
/usr/lib64/R/library/pillar/html/R.css
