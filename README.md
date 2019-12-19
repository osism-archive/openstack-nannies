# openstack-nannies

Various scripts to repair recurring problems in an OpenStack environment.

Usage
-----

* Create `configuration/clouds.yml` on basis of `configuration/clouds.yml.sample`
* Create `configuration/secure.yml` on basis of `configuration/secure.yml.sample`
* Create `configuration/nova.env` on basis of `configuration/nova.env.sample`
* Optionally edit the file `files/crontab`
* Build the container image with `docker-compose build`
* Start the container with `docker-compose up -d`

Sources
-------

The scripts partly originate from other projects. The exact source is mentioned in the
first lines of the scripts.

* https://github.com/cernops/nova-quota-sync
* https://github.com/sapcc/openstack-nannies
