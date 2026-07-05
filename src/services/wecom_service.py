from __future__ import annotations

import os
import requests
from dotenv import load_dotenv


def send_daily_report():
    load_dotenv()

    corp_id = os.getenv("WECOM_CORP_ID")
    agent_id = os.getenv("WECOM_AGENT_ID")
    secret = os.getenv("WECOM_SECRET")
    user_id = os.getenv("WECOM_USER_ID")

    if not all([corp_id, agent_id, secret, user_id]):
        print("企业微信未配置，跳过推送。")
        return

    report_path = "reports/daily_report.md"

    if not os.path.exists(report_path):
        print("未找到日报文件。")
        return

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()[:1500]

    try:
        token_url = (
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            f"?corpid={corp_id}&corpsecret={secret}"
        )

        token_resp = requests.get(token_url, timeout=15).json()
        print("企业微信 token 返回：", token_resp)

        token = token_resp.get("access_token")
        if not token:
            print("企业微信 access_token 获取失败，请检查 WECOM_CORP_ID 和 WECOM_SECRET。")
            return

        send_url = (
            "https://qyapi.weixin.qq.com/cgi-bin/message/send"
            f"?access_token={token}"
        )

        data = {
            "touser": user_id,
            "msgtype": "text",
            "agentid": int(agent_id),
            "text": {
                "content": "📈 Stone AI 每日投资报告\n\n" + content
            },
            "safe": 0,
        }

        send_resp = requests.post(send_url, json=data, timeout=15).json()
        print("企业微信推送返回：", send_resp)

    except Exception as e:
        print("企业微信发送失败：", e)
