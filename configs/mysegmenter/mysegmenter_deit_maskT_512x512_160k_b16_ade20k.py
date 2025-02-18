_base_ = [
    '../_base_/models/MySegmenter.py',
    '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_160k.py'
]
find_unused_parameters = True
norm_cfg = dict(type='SyncBN', requires_grad=True)
model = dict(
    backbone=dict(img_size=(512, 512),
                  drop_rate=0.,
                  drop_path_rate=0.1), # deit-spectific

    test_cfg=dict(mode='slide', crop_size=(512, 512), stride=(341, 341)),
    )

optimizer = dict(
    lr=0.001,
    weight_decay=0.0,
    paramwise_cfg=dict(custom_keys={'head': dict(lr_mult=10.)})) # todo?

# num_gpus: 8 -> batch_size: 8
data = dict(samples_per_gpu=4)
