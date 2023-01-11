# ginfo

A versatile tool for discovering Grid services by querying LDAP-based Grid
information services.

BDII documentation is available at
[gridinfo documentation site](https://gridinfo-documentation.readthedocs.io/).

## Installing from packages

### On RHEL-based systems

On RHEL-based systems, it's possible to install packages from EPEL or
[EGI UMD packages](https://go.egi.eu/umd).

The UMD packages are built automatically from this repository, and tested to
work with other components part of the Unified Middleware Distribution.

## Building packages

A Makefile allowing to build source tarball and packages is provided.

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync
- python
- python-ldap

```shell
# Checkout tag to be packaged
$ git clone https://github.com/EGI-Foundation/ginfo.git
$ cd ginfo
$ git checkout X.X.X
# Building in a container
$ docker run --rm -v $(pwd):/source -it quay.io/centos/centos:7
[root@8a9d60c61f42 /]# cd /source
[root@8a9d60c61f42 /]# yum install -y rpm-build yum-utils
[root@8a9d60c61f42 /]# yum-builddep -y ginfo.spec
[root@8a9d60c61f42 /]# make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Installing from source

This procedure is not recommended for production deployment, please consider
using packages.

- Build dependencies: None
- Runtime dependencies: python, python-ldap

Get the source by cloning this repository and do a `make install`.

## Usage

See usage in the manpage ([ginfo (1)](man/ginfo.1)).

```shell
# List all information for all Endpoint attributes
ginfo --host lcg-bdii.egi.eu Endpoint

# Use the host from the LCG_GFAL_INFOSYS environment variable and list all Location countries
export LCG_GFAL_INFOSYS=lcg-bdii.egi.eu:2170
ginfo Location Country

# List all the Service types
ginfo -l Type Service

# List all IDs from Endpoint which have 'bdii_top' as name of Interface
ginfo Endpoint InterfaceName=bdii_top ID

# Show the version too
ginfo Endpoint InterfaceName=bdii_top ID InterfaceVersion

# Show all available information about these Endpoints"
ginfo Endpoint InterfaceName=bdii_top

# Export to JSON
ginfo --json Endpoint InterfaceName=bdii_top
```

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in
    - [CHANGELOG](CHANGELOG)
    - [ginfo.spec](ginfo.spec)
    - [debian/changelog](debian/changelog)
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
