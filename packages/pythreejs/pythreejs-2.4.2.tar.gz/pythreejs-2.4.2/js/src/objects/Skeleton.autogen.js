//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;

var BoneModel = require('./Bone.autogen.js').BoneModel;

class SkeletonModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            bones: [],

        });
    }

    constructThreeObject() {

        var result = new THREE.Skeleton(
            this.convertThreeTypeArrayModelToThree(this.get('bones'), 'bones')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.three_nested_properties.push('bones');


        this.property_converters['bones'] = 'convertThreeTypeArray';


    }
}

SkeletonModel.model_name = 'SkeletonModel';
SkeletonModel.serializers = {
    ...ThreeModel.serializers,
    bones: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    SkeletonModel: SkeletonModel,
};
