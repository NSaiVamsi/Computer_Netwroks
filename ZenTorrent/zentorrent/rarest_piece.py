import logging



class RarestPieces(object):
    def __init__(self, pieces_manager):

        self.pieces_manager = pieces_manager
        self.rarest_pieces = []
        self.visited = []

        for piece in self.pieces_manager.pieces:
            self.rarest_pieces.append({"idPiece": piece.piece_index, "numberOfPeers": 0, "peers": []})

        # pub.subscribe(self.peersBitfield, 'RarestPiece.updatePeersBitfield')

    # def peers_bitfield(self, peer, piece_index):
    #     if not peer or piece_index is None:
    #         logging.error("Invalid peer or piece_index in peers_bitfield method.")
    #         return

    #     if not self.pieces_manager.pieces[piece_index].are_all_blocks_full():
    #         if peer not in self.rarest_pieces[piece_index]["peers"]:
    #             self.rarest_pieces[piece_index]["peers"].append(peer)
    #             self.rarest_pieces[piece_index]["numberOfPeers"] = len(self.rarest_pieces[piece_index]["peers"])

    # def get_sorted_pieces(self):
    #     return sorted(self.rarest_pieces, key=lambda x: x['numberOfPeers'])

    def peers_bitfield(self,peer=None, piece_index=None):

        if len(self.rarest_pieces) == 0:
            raise Exception("No more piece")

        # Piece complete
        # try:
        #     if not piece_index == None:
        #         self.rarest_pieces.__delitem__(piece_index)
        # except Exception:
        #         logging.exception("Failed to remove rarest piece")

        # Peer's bitfield updated
        else:
            if peer.has_piece(piece_index) == 1 and peer not in self.rarest_pieces[piece_index]["peers"]:
                    self.rarest_pieces[piece_index]["peers"].append(peer)
                    self.rarest_pieces[piece_index]["numberOfPeers"] = len(self.rarest_pieces[piece_index]["peers"])

            # for i in range(len(self.rarest_pieces)):
            #     if peer.has_piece(piece_index) == 1 and peer not in self.rarest_pieces[i]["peers"]:
            #         self.rarest_pieces[i]["peers"].append(peer)
            #         self.rarest_pieces[i]["numberOfPeers"] = len(self.rarest_pieces[i]["peers"])
                
    def get_sorted_pieces(self,counter):
        sorted_pieces = sorted(self.rarest_pieces, key=lambda x: x['numberOfPeers'])
        popped_elements = []
        for i in range(0,counter+1):
            if sorted_pieces:  # Check if there are still elements to pop
                popped_elements.append(sorted_pieces.pop(0))

        logging.info(f'{len(popped_elements)-1}')         
        return popped_elements[len(popped_elements)-1]

    def nget_sorted_pieces(self,peers,pieces):
        list = [ ] 
        for piece in pieces:
            dic = { "piece" : piece , "value" : 0 }
            for peer in peers:
                if(peer.has_piece(piece.index)):
                    dic["value"] += 1     
            list.append(dic) 
        
        sorted_data = sorted(list, key=lambda x: x["value"])
        sorted_piece_list = []
        for  d in sorted_data:
            sorted_piece_list.append(d["piece"])
        return sorted_piece_list    