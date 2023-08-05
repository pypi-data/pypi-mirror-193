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


class AnimationMixerModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            rootObject: null,
            time: 0,
            timeScale: 1,

        });
    }

    constructThreeObject() {

        var result = new THREE.AnimationMixer(
            this.convertThreeTypeModelToThree(this.get('rootObject'), 'rootObject'),
            this.convertFloatModelToThree(this.get('time'), 'time'),
            this.convertFloatModelToThree(this.get('timeScale'), 'timeScale')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('rootObject');


        this.property_converters['rootObject'] = 'convertThreeType';
        this.property_converters['time'] = 'convertFloat';
        this.property_converters['timeScale'] = 'convertFloat';


    }
}

AnimationMixerModel.model_name = 'AnimationMixerModel';
AnimationMixerModel.serializers = {
    ...ThreeModel.serializers,
    rootObject: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    AnimationMixerModel: AnimationMixerModel,
};
