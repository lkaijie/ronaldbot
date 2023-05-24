import os
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import asyncio
import config
import random




class LevelerDB():
    def __init__(self) -> None:
        cred = credentials.Certificate(config.firebase_config)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    async def level_up(self, user_id):
        user = self.db.collection("SIUers").document(str(user_id))
        user_data = user.get()
        if user_data.exists:
            user_data = user_data.to_dict()
            user_data["player_level"] += 1
            user_data["xp"] = 0
            user_data["next_level_xp"] = user_data["player_level"] * 100
            user.set(user_data)
            return user_data["player_level"]
        else:
            print("User not found")
            return False
        
    async def add_xp(self, user_id, xp, rare=False, SIUUUUUUUUU=False, player_name=None):
        user = self.db.collection("SIUers").document(str(user_id))
        user_data = user.get()
        level_up = False
        if user_data.exists:
            user_data = user_data.to_dict()
            if random.randint(1, 100) <= 5:
                xp *= 2
            if SIUUUUUUUUU:
                xp *= 50
                user_data["times_siued"] += 1
            user_data["xp"] += xp
            user_data["messages_sent"] += 1
            user.set(user_data)
            if user_data["xp"] >= user_data["next_level_xp"]:
                await self.level_up(user_id)
                level_up = True
            return level_up, user_data["xp"], user_data["next_level_xp"],user_data["player_level"]
        else:
            print("User not found")
            print("Creating user...")
            # player_name = await self.get_name(user_id)
            user_data = {
                "player_level": 1,
                "xp": 1,
                "next_level_xp": 100,
                "times_siued": 0,
                "player_name": player_name if player_name else "Unknown",
                "messages_sent": 1,
            }
            if SIUUUUUUUUU:
                user_data["times_siued"] += 1
                user_data["xp"] += 49
            user.set(user_data)
            return False
    async def get_progress(self, user_id):
        user = self.db.collection("SIUers").document(str(user_id))
        user_data = user.get()
        if user_data.exists:
            user_data = user_data.to_dict()
            return user_data["xp"], user_data["next_level_xp"], user_data["player_level"],user_data["times_siued"], user_data["player_name"], user_data["messages_sent"]
        else:
            print("User not found")
            return False
    async def get_rank(self, user_id):
        user = self.db.collection("SIUers").document(str(user_id))
        user_data = user.get()
        if user_data.exists:
            user_data = user_data.to_dict()
            rank = 1
            siu_rank = 1
            for x in self.db.collection("SIUers").stream():
                x = x.to_dict()
                if int(x["player_level"]) > int(user_data["player_level"]):
                    rank += 1
                if int(x["times_siued"]) > int(user_data["times_siued"]):
                    siu_rank += 1
            return rank, siu_rank
        else:
            print("User not found")
            return False
    
    
    def get_leaderboard(self):
        leaderboard = []
        for x in self.db.collection("SIUers").stream():
            x = x.to_dict()
            leaderboard.append([x["player_name"], x["player_level"]])
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        return leaderboard
    
    def get_leaderboard_siu(self):
        leaderboard = []
        for x in self.db.collection("SIUers").stream():
            x = x.to_dict()
            leaderboard.append([x["player_name"], x["times_siued"]])
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        return leaderboard