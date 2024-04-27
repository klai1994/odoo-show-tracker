# -*- coding: utf-8 -*-

from odoo import api, models, fields

class ShowTracker(models.Model):
    _name = 'show.tracker'
    _inherit= 'mail.thread'
    _description = 'Show Tracker'

    name = fields.Text(string="Show Name")
    watched_episodes = fields.Integer(string="Watched Episodes", default=0)
    total_episodes = fields.Integer(string="Total Episodes")

    status = fields.Selection(string="Status", 
        selection=[
        ('plan_to_watch', 'Plan to Watch'), 
        ('currently_watching', 'Currently Watching'),
        ('on_hold', 'On Hold'),
        ('dropped', 'Dropped'),
        ('completed', 'Completed')
        ], default="plan_to_watch"
    )
    
    rating = fields.Selection(string="Rating",
        selection=[
        ('0', 'No Rating'),
        ('1', 'Terrible'),
        ('2', 'Not Good'),
        ('3', 'OK'),
        ('4', 'Good'),
        ('5', 'Awesome!')],
    )
