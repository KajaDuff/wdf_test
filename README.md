# wdf_test

# note:
cmsplugin_plain_text requires following update in cmsplugin_plain_text/migrations/0001_initial.py:

fields=[
            ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True,primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=modelsCASCADE)),
            ('body', models.TextField(verbose_name='Plaintext')),
        ],