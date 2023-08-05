====================================
django app of an organization
====================================

Anorganization uses membership, and organization models to group users.
Support for Ariadne graphQL with pre-defined types and basic resolvers.

------------
Requirements
------------

* Python 3.10+
* django 4.0+
* ariadne 0.16.0+
* ariadne-relay 0.1.0a8+
* pillow 9.4.0+

--------
Settings
--------
Store uploaded file with tokenize file name, default to False

* ANORGANIZATION_USE_TOKEN_FILENAME = True

-------------------
Django admin mixins
-------------------

Use predefined mixins to construct the admin class.

* OrganizationAdminMixin
* MembershipAdminMixin

.. code:: python

    from django.contrib import admin

    from anorganization.models import Organization
    from anorganization.mixins import OrganizationAdminMixin


    @admin.register(Organization)
    class OrganizationAdmin(OrganizationAdminMixin, ModelAdmin):
        ...

---------------------------
Ariadne types and resolvers
---------------------------

Integrate predefined types and resolvers to scheme.

**resolvers**

* resolve_anorganizations
* resolve_anorganization_memberships

**types**

* anorganization
* anorganization_membership

**graphql**

* anorganization/graphqls/organization.graphql
* anorganization/graphqls/membership.graphql

-------
License
-------

django-anarticle is released under the terms of **Apache license**. Full details in LICENSE file.
