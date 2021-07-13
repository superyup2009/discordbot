# discord 라이브러리 사용 선언
import discord


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("물의 호흡 ")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None
        
        # message.content = message의 내용
        if message.content == "!기유야 물의호흡 3형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제3형 유유 춤."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 4형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제4형 들이친 파도."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 1형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제1형 수면 베기."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 2형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제2형 물방아."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 5형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제5형 가뭄의 단비."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 6형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제6형 비틀린 소용돌이."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 7형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제7형 물방울 파문 찌르기."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 8형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제8형 용소."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 9형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제9형 수류 물보라 란."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 10형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제10형 생생유전."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 물의호흡 11형":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제11형 잔잔한 물결, 이건 나만 쓸수 있지."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 안녕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "난 수다를 떠는건 좋아하지 않아."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 탄지로":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "탄지로는 내게 실망을 줬어...."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!기유야 이름":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "난 토미오카 기유다."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
            
            
            
        
        
        # 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("ODY0Mjg4MTEwNjE1MzMwODU2.YOzRBw.PdtusfGE9sKCy0QCLhYFuVXmHkE")
