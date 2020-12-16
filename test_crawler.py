import crawler

def test_run():
    data = crawler.run()
    assert len(data) > 0

