import os
import configparser
from odoo.cli.shell import Shell
from contextlib import contextmanager


@contextmanager
def get_odoo_env(odoo_config_file, dbname, odoo_dir=None):
    if not odoo_dir:
        config = configparser.ConfigParser()
        config.read(odoo_config_file)
        addons = config['options']['addons_path'].split(',')
        odoo_addons = [x for x in addons if x.endswith('odoo/addons')]
        for odoo_addon in odoo_addons:
            if os.path.exists(os.path.join(odoo_addon, os.pardir, 'odoo-bin')):
                odoo_dir = os.path.abspath(os.path.join(odoo_addon, os.pardir))
                break
        if not odoo_dir:
            raise Exception("Unable to detect odoo_dir, please specify odoo directory")
    os.sys.path.insert(0, odoo_dir)

    parent_dir = os.path.abspath(os.path.join(odoo_dir, os.pardir))
    os.sys.path.insert(0, parent_dir)


    odoo_args = ['-c', odoo_config_file, '--stop-after-init', '--no-xmlrpc']

    task = Task()
    task.init(odoo_args)
    with task.get_env(dbname) as env:
        yield env

class Task(Shell):
    @contextmanager
    def get_env(self, dbname):
        import odoo
        with odoo.api.Environment.manage():
            registry = odoo.registry(dbname)
            with registry.cursor() as cr:
                uid = odoo.SUPERUSER_ID
                ctx = odoo.api.Environment(cr, uid, {})['res.users'].context_get()
                env = odoo.api.Environment(cr, uid, ctx)
                yield env
