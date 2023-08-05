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


class PlaneModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            normal: [0,0,0],
            constant: 0,

        });
    }

    constructThreeObject() {

        var result = new THREE.Plane(
            this.convertVectorModelToThree(this.get('normal'), 'normal'),
            this.convertFloatModelToThree(this.get('constant'), 'constant')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['normal'] = 'convertVector';
        this.property_converters['constant'] = 'convertFloat';

        this.property_assigners['normal'] = 'assignVector';

    }
}

PlaneModel.model_name = 'PlaneModel';
PlaneModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    PlaneModel: PlaneModel,
};
