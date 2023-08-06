from pathlib import Path
from smtplib import SMTPServerDisconnected

from pytest import raises

from utilities.airium import yield_airium
from utilities.email import InvalidContentsError, send_email


class TestSendEmail:
    def test_main(self) -> None:
        with raises(SMTPServerDisconnected):
            send_email("no-reply@test.com", ["user@test.com"])

    def test_subject(self) -> None:
        with raises(SMTPServerDisconnected):
            send_email(
                "no-reply@test.com",
                ["user@test.com"],
                subject="Subject",
            )

    def test_contents_str(self) -> None:
        with raises(SMTPServerDisconnected):
            send_email(
                "no-reply@test.com",
                ["user@test.com"],
                subject="Subject",
                contents="contents",
            )

    def test_contents_airium(self) -> None:
        with yield_airium() as airium:
            _ = airium
        with raises(SMTPServerDisconnected):
            send_email(
                "no-reply@test.com",
                ["user@test.com"],
                subject="Subject",
                contents=airium,
            )

    def test_attachment(self, tmp_path: Path) -> None:
        file = tmp_path.joinpath("file")
        file.touch()
        with raises(SMTPServerDisconnected):
            send_email(
                "no-reply@test.com",
                ["user@test.com"],
                subject="Subject",
                attachments=[file],
            )

    def test_invalid_contents(self) -> None:
        with raises(InvalidContentsError):
            send_email(
                "no-reply@test.com",
                ["user@test.com"],
                subject="Subject",
                contents=object(),
            )
