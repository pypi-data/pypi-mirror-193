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


class SphereModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            center: [0,0,0],
            radius: 0,

        });
    }

    constructThreeObject() {

        var result = new THREE.Sphere(
            this.convertVectorModelToThree(this.get('center'), 'center'),
            this.convertFloatModelToThree(this.get('radius'), 'radius')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['center'] = 'convertVector';
        this.property_converters['radius'] = 'convertFloat';

        this.property_assigners['center'] = 'assignVector';

    }
}

SphereModel.model_name = 'SphereModel';
SphereModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    SphereModel: SphereModel,
};
