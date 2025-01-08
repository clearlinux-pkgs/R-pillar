#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-pillar
Version  : 1.10.1
Release  : 75
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/pillar_1.10.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/pillar_1.10.1.tar.gz
Summary  : Coloured Formatting for Columns
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-glue
Requires: R-lifecycle
Requires: R-rlang
Requires: R-utf8
Requires: R-vctrs
BuildRequires : R-cli
BuildRequires : R-glue
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : R-utf8
BuildRequires : R-vctrs
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
for formatting columns of data using the full range of colours
    provided by modern terminals.

%prep
%setup -q -n pillar
pushd ..
cp -a pillar buildavx2
popd
pushd ..
cp -a pillar buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736350368

%install
export SOURCE_DATE_EPOCH=1736350368
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pillar/DESCRIPTION
/usr/lib64/R/library/pillar/INDEX
/usr/lib64/R/library/pillar/LICENSE
/usr/lib64/R/library/pillar/Meta/Rd.rds
/usr/lib64/R/library/pillar/Meta/features.rds
/usr/lib64/R/library/pillar/Meta/hsearch.rds
/usr/lib64/R/library/pillar/Meta/links.rds
/usr/lib64/R/library/pillar/Meta/nsInfo.rds
/usr/lib64/R/library/pillar/Meta/package.rds
/usr/lib64/R/library/pillar/Meta/vignette.rds
/usr/lib64/R/library/pillar/NAMESPACE
/usr/lib64/R/library/pillar/NEWS.md
/usr/lib64/R/library/pillar/R/pillar
/usr/lib64/R/library/pillar/R/pillar.rdb
/usr/lib64/R/library/pillar/R/pillar.rdx
/usr/lib64/R/library/pillar/WORDLIST
/usr/lib64/R/library/pillar/doc/debugme.R
/usr/lib64/R/library/pillar/doc/debugme.Rmd
/usr/lib64/R/library/pillar/doc/debugme.html
/usr/lib64/R/library/pillar/doc/digits.Rmd
/usr/lib64/R/library/pillar/doc/digits.html
/usr/lib64/R/library/pillar/doc/extending.R
/usr/lib64/R/library/pillar/doc/extending.Rmd
/usr/lib64/R/library/pillar/doc/extending.html
/usr/lib64/R/library/pillar/doc/index.html
/usr/lib64/R/library/pillar/doc/numbers.R
/usr/lib64/R/library/pillar/doc/numbers.Rmd
/usr/lib64/R/library/pillar/doc/numbers.html
/usr/lib64/R/library/pillar/doc/printing.R
/usr/lib64/R/library/pillar/doc/printing.Rmd
/usr/lib64/R/library/pillar/doc/printing.html
/usr/lib64/R/library/pillar/help/AnIndex
/usr/lib64/R/library/pillar/help/aliases.rds
/usr/lib64/R/library/pillar/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/pillar/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/pillar/help/paths.rds
/usr/lib64/R/library/pillar/help/pillar.rdb
/usr/lib64/R/library/pillar/help/pillar.rdx
/usr/lib64/R/library/pillar/html/00Index.html
/usr/lib64/R/library/pillar/html/R.css
/usr/lib64/R/library/pillar/tests/testthat.R
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ansi/ctl_colonnade.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ctl_colonnade.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ctl_colonnade_1.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ctl_colonnade_2.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ctl_compound.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ctl_new_pillar.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_asis.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_character.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_date.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_decimal.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_factor.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_integer.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_integer64.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_list.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_list_of.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_logical.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_lubridate.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_numeric.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_rowid.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_scientific.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_survival.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_time.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/format_unspecified.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ggplot2/basic.svg
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ggplot2/log-scale.svg
/usr/lib64/R/library/pillar/tests/testthat/_snaps/glimpse.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/multi.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/num.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ornament.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/rowid.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/shaft-.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/tbl-format-body.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/tbl-format-footer.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/tbl-format-header.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/tbl-format-setup.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/tbl-format.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/testthat_3.1.2/tbl-format.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/testthat_3.1.3/tbl-format.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/ticks.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/title.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/type_sum.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/unicode/ctl_colonnade.md
/usr/lib64/R/library/pillar/tests/testthat/_snaps/vctr.md
/usr/lib64/R/library/pillar/tests/testthat/helper-foo-tbl.R
/usr/lib64/R/library/pillar/tests/testthat/helper-methods.R
/usr/lib64/R/library/pillar/tests/testthat/helper-output.R
/usr/lib64/R/library/pillar/tests/testthat/helper-size-sum.R
/usr/lib64/R/library/pillar/tests/testthat/helper-snapshot.R
/usr/lib64/R/library/pillar/tests/testthat/helper-tbl-sum.R
/usr/lib64/R/library/pillar/tests/testthat/helper-testthat.R
/usr/lib64/R/library/pillar/tests/testthat/helper-type-sum.R
/usr/lib64/R/library/pillar/tests/testthat/helper-unknown-rows.R
/usr/lib64/R/library/pillar/tests/testthat/setup.R
/usr/lib64/R/library/pillar/tests/testthat/test-ctl_colonnade.R
/usr/lib64/R/library/pillar/tests/testthat/test-ctl_colonnade_1.R
/usr/lib64/R/library/pillar/tests/testthat/test-ctl_colonnade_2.R
/usr/lib64/R/library/pillar/tests/testthat/test-ctl_compound.R
/usr/lib64/R/library/pillar/tests/testthat/test-ctl_new_pillar.R
/usr/lib64/R/library/pillar/tests/testthat/test-dim.R
/usr/lib64/R/library/pillar/tests/testthat/test-distribute.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_asis.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_character.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_date.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_decimal.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_factor.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_integer.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_integer64.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_list.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_list_of.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_logical.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_lubridate.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_numeric.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_rowid.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_scientific.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_survival.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_time.R
/usr/lib64/R/library/pillar/tests/testthat/test-format_unspecified.R
/usr/lib64/R/library/pillar/tests/testthat/test-ggplot2.R
/usr/lib64/R/library/pillar/tests/testthat/test-glimpse.R
/usr/lib64/R/library/pillar/tests/testthat/test-multi.R
/usr/lib64/R/library/pillar/tests/testthat/test-new-pillar-title.R
/usr/lib64/R/library/pillar/tests/testthat/test-new-pillar-type.R
/usr/lib64/R/library/pillar/tests/testthat/test-num.R
/usr/lib64/R/library/pillar/tests/testthat/test-obj-sum.R
/usr/lib64/R/library/pillar/tests/testthat/test-options.R
/usr/lib64/R/library/pillar/tests/testthat/test-ornament.R
/usr/lib64/R/library/pillar/tests/testthat/test-rowid.R
/usr/lib64/R/library/pillar/tests/testthat/test-shaft-.R
/usr/lib64/R/library/pillar/tests/testthat/test-tbl-format-body.R
/usr/lib64/R/library/pillar/tests/testthat/test-tbl-format-footer.R
/usr/lib64/R/library/pillar/tests/testthat/test-tbl-format-header.R
/usr/lib64/R/library/pillar/tests/testthat/test-tbl-format-setup.R
/usr/lib64/R/library/pillar/tests/testthat/test-tbl-format.R
/usr/lib64/R/library/pillar/tests/testthat/test-ticks.R
/usr/lib64/R/library/pillar/tests/testthat/test-title.R
/usr/lib64/R/library/pillar/tests/testthat/test-type_sum.R
/usr/lib64/R/library/pillar/tests/testthat/test-vctr.R
