import sublime
import sublime_plugin
import re

from Context.base import Base

class Scope(Base):
  def on_query_context(self, *args):
    callback_left = lambda view, sel: view.scope_name(sel.begin())
    callback_right = lambda view, sel: view.scope_name(sel.end() - 1)

    result = (
      self._check_sel('scope', callback_right, *args) and
      (sel.empty() or self._check_sel('scope', callback_left, *args))
    )

    return result

class ScopeB(Base):
  def on_query_context(self, *args):
    callback_right = lambda view, sel: view.scope_name(sel.b)
    callback_left = lambda view, sel: view.scope_name(sel.b - 1)

    result = (
      self._check_sel('scope_b', callback_left, *args) and
      self._check_sel('scope_b', callback_right, *args)
    )

    return result

class ScopeA(Base):
  def on_query_context(self, *args):
    callback_right = lambda view, sel: view.scope_name(sel.a)
    callback_left = lambda view, sel: view.scope_name(sel.a - 1)

    result = (
      self._check_sel('scope_a', callback_left, *args) and
      self._check_sel('scope_a', callback_right, *args)
    )

    return result

class ScopeBRight(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.scope_name(sel.b)
    return self._check_sel('scope_b_right', callback, *args)

class ScopeBLeft(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.scope_name(sel.b - 1)
    return self._check_sel('scope_b_left', callback, *args)

class ScopeARight(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.scope_name(sel.a)
    return self._check_sel('scope_a_right', callback, *args)

class ScopeALeft(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.scope_name(sel.a - 1)
    return self._check_sel('scope_a_left', callback, *args)

class ScopeLeft(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.scope_name(sel.begin() - 1)
    return self._check_sel('scope_left', callback, *args)

class ScopeRight(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.scope_name(sel.end())
    return self._check_sel('scope_right', callback, *args)