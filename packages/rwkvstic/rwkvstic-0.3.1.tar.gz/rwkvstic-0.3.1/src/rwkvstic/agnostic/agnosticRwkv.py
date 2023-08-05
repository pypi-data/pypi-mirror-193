from rwkvstic.agnostic.backends.base import module
from typing import Dict


def AgnostigRWKV(ops: module, *args):
    class myRWKV(ops.module):

        @ ops.initfunc
        def __init__(self, w: Dict[str, ops.TensorType]):
            super(myRWKV, self).__init__()

            self.ops = ops
            self.postprocess0: ops.VectorType = (w["ln_out.weight"])
            self.postprocess1: ops.VectorType = (w["ln_out.bias"])
            self.postprocess2: ops.VectorType = (w["head.weight"])
            self.emb: ops.MatrixType = w["emb.weight"]
            self.emb1: ops.VectorType = w["blocks.0.ln0.weight"]
            self.emb2: ops.VectorType = w["blocks.0.ln0.bias"]
            self.ln1w: ops.VectorType = ops.stack(
                [w[f"blocks.{x}.ln1.weight"] for x in range(ops.n_layers)])
            self.ln1b: ops.VectorType = ops.stack(
                [w[f"blocks.{x}.ln1.bias"] for x in range(ops.n_layers)])
            self.ln2w: ops.VectorType = ops.stack(
                [w[f"blocks.{x}.ln2.weight"] for x in range(ops.n_layers)])
            self.ln2b: ops.VectorType = ops.stack(
                [w[f"blocks.{x}.ln2.bias"] for x in range(ops.n_layers)])
            self.time_decay: ops.VectorType = ops.stack([
                w[f"blocks.{x}.att.time_decay"] for x in range(ops.n_layers)])
            self.time_first: ops.VectorType = ops.stack([
                w[f"blocks.{x}.att.time_first"] for x in range(ops.n_layers)])
            self.kktk: ops.VectorType = ops.stack(
                [w[f"blocks.{x}.att.time_mix_k"] for x in range(ops.n_layers)])
            self.vvtv: ops.VectorType = ops.stack(
                [w[f"blocks.{x}.att.time_mix_v"] for x in range(ops.n_layers)])
            self.rrtr: ops.VectorType = ops.stack(
                [w[f"blocks.{x}.att.time_mix_r"] for x in range(ops.n_layers)])
            self.key: ops.MatrixType = ops.stack(
                [w[f"blocks.{x}.att.key.weight"] for x in range(ops.n_layers)])
            self.value: ops.MatrixType = ops.stack(
                [w[f"blocks.{x}.att.value.weight"] for x in range(ops.n_layers)])
            self.receptance: ops.MatrixType = ops.stack([
                w[f"blocks.{x}.att.receptance.weight"] for x in range(ops.n_layers)])
            self.outputvv: ops.MatrixType = ops.stack([
                w[f"blocks.{x}.att.output.weight"] for x in range(ops.n_layers)])
            self.time_mix_k_ffn: ops.VectorType = ops.stack([
                w[f"blocks.{x}.ffn.time_mix_k"] for x in range(ops.n_layers)])
            self.time_mix_r_ffn: ops.VectorType = ops.stack([
                w[f"blocks.{x}.ffn.time_mix_r"] for x in range(ops.n_layers)])
            self.key_ffn: ops.MatrixType = ops.stack(
                [w[f"blocks.{x}.ffn.key.weight"] for x in range(ops.n_layers)])
            self.receptance_ffn: ops.MatrixType = ops.stack([
                w[f"blocks.{x}.ffn.receptance.weight"] for x in range(ops.n_layers)])
            self.value_ffn: ops.MatrixType = ops.stack([
                w[f"blocks.{x}.ffn.value.weight"] for x in range(ops.n_layers)])

        @ops.layerdef
        def doLayer(self, x, statea, stateb, statec, stated, xx):
            xy = ops.layernorm(x, self.ln1w[xx], self.ln1b[xx])

            kk = ops.matvec(
                self.key[xx], ops.lerp(statea, xy, self.kktk[xx]))

            v = ops.matvec(self.value[xx], ops.lerp(
                statea, xy, self.vvtv[xx]))

            r = ops.logistical(ops.matvec(
                self.receptance[xx], ops.lerp(statea, xy, self.rrtr[xx])))

            kt = ops.exp(ops.minimum(
                ops.add(kk, self.time_first[xx]), ops.klimit))
            k = ops.exp(ops.minimum(kk, ops.klimit))

            wrd = ops.divide(
                ops.add(stateb, ops.multiply(kt, v)), ops.add(statec, kt))
            outb = ops.add(ops.multiply(
                stateb, self.time_decay[xx]), ops.multiply(k, v))
            outc = ops.add(ops.multiply(statec, self.time_decay[xx]), k)

            mvv = ops.add(x, ops.matvec(
                self.outputvv[xx], ops.multiply(r, wrd)))

            ddd = ops.layernorm(mvv, self.ln2w[xx], self.ln2b[xx])

            km = ops.relu(ops.matvec(self.key_ffn[xx], ops.lerp(
                stated, ddd, self.time_mix_k_ffn[xx])))

            rt = ops.logistical(ops.matvec(self.receptance_ffn[xx], ops.lerp(
                stated, ddd, self.time_mix_r_ffn[xx])))

            x = ops.add(mvv, ops.multiply(
                ops.matvec(self.value_ffn[xx], ops.multiply(km, km)), rt))

            return x, xy, outb, outc, ddd

        @ ops.mainfunc
        def forward(self, x: ops.VectorType, state: ops.MatrixType = None):

            if (state is None):
                state = ops.emptyState

            x = ops.layernorm(
                ops.processEmbed(self.emb[x[-1]]), self.emb1, self.emb2)

            statea = state[0::4]
            stateb = state[1::4]
            statec = state[2::4]
            stated = state[3::4]

            ot = []

            for i in range(ops.n_layers):
                x, aaa, bbb, ccc, ddd = self.doLayer(
                    x, statea[i], stateb[i], statec[i], stated[i], i)
                ot = ot + [aaa, bbb, ccc, ddd]

            x = ops.matvec(self.postprocess2, ops.layernorm(x, self.postprocess0,
                                                            self.postprocess1))

            return ops.postProcessTensor(x), ops.stack(ot)

        # for keras stuff, ignore this if you are not using keras
        def call(self, *args, **kwds):
            del kwds["training"]
            return self.forward(*args, **kwds)
    returnObject: myRWKV = ops.postProcessModule(myRWKV(*args))
    return returnObject
