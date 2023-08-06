"""
This file is part of nataili ("Homepage" = "https://github.com/Sygil-Dev/nataili").

Copyright 2022 hlky and Sygil-Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import hashlib

import clip
import numpy as np
import torch

from nataili.cache import Cache
from nataili.util.cast import autocast_cuda
from nataili.util.logger import logger


class TextEmbed:
    def __init__(self, model, cache: Cache):
        """
        :param model: Loaded model from ModelManager
        :param cache: Cache object
        """
        self.model = model
        self.cache = cache

    @autocast_cuda
    def __call__(self, text: str, check_cache: bool = False):
        """
        :param text: Text to embed
        If text is not in cache, embed it and save it to cache
        """
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if check_cache:
            cached = self.cache.get(file_hash=text_hash)
            if cached:
                return cached
        text_tokens = clip.tokenize([text]).cuda()
        with torch.no_grad():
            text_features = self.model["model"].encode_text(text_tokens).float()
        text_features /= text_features.norm(dim=-1, keepdim=True)
        text_embed_array = text_features.cpu().detach().numpy()
        np.save(f"{self.cache.cache_dir}/{text_hash}", text_embed_array)
        self.cache.add_sqlite_row(text, text_hash, text_hash)
