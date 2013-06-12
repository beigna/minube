# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'contacts_group', (
            ('id', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'contacts', ['Group'])

        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            ('id', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding M2M table for field group on 'Contact'
        m2m_table_name = db.shorten_name(u'contacts_contact_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'contacts.contact'], null=False)),
            ('group', models.ForeignKey(orm[u'contacts.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'group_id'])

        # Adding model 'ContactData'
        db.create_table(u'contacts_contactdata', (
            ('id', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length='16')),
            ('label', self.gf('django.db.models.fields.CharField')(max_length='16')),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['ContactData'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'contacts_group')

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Removing M2M table for field group on 'Contact'
        db.delete_table(db.shorten_name(u'contacts_contact_group'))

        # Deleting model 'ContactData'
        db.delete_table(u'contacts_contactdata')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['contacts.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'contacts.contactdata': {
            'Meta': {'object_name': 'ContactData'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': "'16'"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            'id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': "'16'"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'contacts.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['contacts']