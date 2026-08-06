from __future__ import annotations

from xml.sax.saxutils import escape

from flask import Response, current_app, request


def twiml_message(body: str) -> Response:
    xml = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message>{escape(body)}</Message></Response>"
    return Response(xml, mimetype="application/xml")


def validate_twilio_signature() -> bool:
    if not current_app.config.get("VALIDATE_TWILIO_SIGNATURE"):
        return True
    token = current_app.config.get("TWILIO_AUTH_TOKEN")
    if not token:
        return False
    try:
        from twilio.request_validator import RequestValidator
    except ImportError:
        current_app.logger.warning("Twilio package is not installed; cannot validate signature.")
        return False

    validator = RequestValidator(token)
    signature = request.headers.get("X-Twilio-Signature", "")
    public_base = current_app.config.get("PUBLIC_BASE_URL", "").rstrip("/")
    url = public_base + request.path if public_base else request.url
    return validator.validate(url, request.form, signature)
