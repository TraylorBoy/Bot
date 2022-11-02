"""Multithreading & processing worker that executes functions and prints the result"""

from core.bot import Bot

class BotBoy:
  def __init__(self, name, tasks):
    # Creates new bot
    self.bot = Bot(name, tasks)
    self.processing = False

  def display_information(self):
    """Displays the bot's name and tasks"""
    self.bot.get_name()
    self.bot.get_task()

  def set_processing(self):
    """Changes from threading to processing"""
    if self.processing: self.processing = False
    else: self.processing = True

  def execute(self, *args):
    """Runs the bot's assigned task"""
    if not self.processing: self.bot.run_task_on_thread(*args)
    else: self.bot.run_task_on_process(*args)
