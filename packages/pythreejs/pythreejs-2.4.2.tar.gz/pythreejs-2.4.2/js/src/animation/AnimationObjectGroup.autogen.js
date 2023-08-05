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


class AnimationObjectGroupModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.AnimationObjectGroup();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);




    }
}

AnimationObjectGroupModel.model_name = 'AnimationObjectGroupModel';
AnimationObjectGroupModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    AnimationObjectGroupModel: AnimationObjectGroupModel,
};
