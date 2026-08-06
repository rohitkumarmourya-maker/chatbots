def send(client, text, phone="test:+910000000001"):
    return client.post("/api/demo/message", json={"message": text, "phone": phone}).get_json()["reply"]


def test_menu_reply(client):
    reply = send(client, "menu")
    assert "Today's Menu" in reply
    assert "PZ01" in reply


def test_order_flow(client):
    reply = send(client, "order")
    assert "Today's Menu" in reply
    reply = send(client, "PZ01 x2, BR01 x1")
    assert "Your Cart" in reply
    reply = send(client, "done")
    assert "delivery address" in reply.lower()
    reply = send(client, "221B Baker Street, Pune")
    assert "Payment" in reply
    reply = send(client, "cash")
    assert "Order confirmed" in reply
    assert "ORD-" in reply


def test_booking_flow(client):
    assert "booking name" in send(client, "book").lower()
    assert "date and time" in send(client, "Rohit").lower()
    assert "how many" in send(client, "tomorrow 7pm").lower()
    reply = send(client, "4")
    assert "Booking confirmed" in reply
    assert "BK-" in reply


def test_lead_flow(client):
    assert "staff" in send(client, "human").lower()
    reply = send(client, "Rohit, catering for 40 people, rohit@example.com")
    assert "shared with our staff" in reply
