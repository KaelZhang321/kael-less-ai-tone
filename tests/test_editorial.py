import importlib.util
from pathlib import Path
import unittest
p=Path(__file__).resolve().parents[1]/'scripts/editorial_qa.py'
s=importlib.util.spec_from_file_location('qa',p);q=importlib.util.module_from_spec(s);s.loader.exec_module(q)
class EditorialTests(unittest.TestCase):
 def test_clean(self):self.assertEqual(q.analyze('这个接口返回 JSON。'),[])
 def test_staging(self):self.assertTrue(q.analyze('接下来让我们分析。'))
 def test_same(self):self.assertTrue(q.compare('接口有 3 个参数。','接口有 3 个参数。')['mechanical_checks_pass'])
 def test_numbers(self):self.assertIn('numeric_token_change',q.compare('有 3 个','有 4 个')['issues'])
 def test_heading(self):self.assertIn('heading_change',q.compare('## A\n内容','## B\n内容')['issues'])
 def test_quote(self):self.assertIn('protected_span_change',q.compare('他说「尚未测试」','他说「已经完成」')['issues'])
 def test_code(self):self.assertIn('protected_span_change',q.compare('`run x`','`run y`')['issues'])
 def test_url(self):self.assertIn('protected_span_change',q.compare('https://example.org/a','https://example.org/b')['issues'])
 def test_frontmatter(self):self.assertIn('protected_span_change',q.compare('---\ntitle: A\n---\n正文','---\ntitle: B\n---\n正文')['issues'])
 def test_limitation(self):self.assertTrue(q.compare('可能有效','已经有效')['semantic_review_required'])
if __name__=='__main__':unittest.main()
