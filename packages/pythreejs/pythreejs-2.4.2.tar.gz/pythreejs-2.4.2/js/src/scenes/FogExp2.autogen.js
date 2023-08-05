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


class FogExp2Model extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            name: "",
            color: "white",
            density: 0.00025,

        });
    }

    constructThreeObject() {

        var result = new THREE.FogExp2(
            this.convertColorModelToThree(this.get('color'), 'color'),
            this.convertFloatModelToThree(this.get('density'), 'density')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['name'] = null;
        this.property_converters['color'] = 'convertColor';
        this.property_converters['density'] = 'convertFloat';


    }
}

FogExp2Model.model_name = 'FogExp2Model';
FogExp2Model.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    FogExp2Model: FogExp2Model,
};
